from conans import CMake, ConanFile
from conans.tools import replace_in_file


class BloscConan(ConanFile):
    description = "A blocking, shuffling and lossless compression library"
    name = "blosc"
    version = "1.11.2"
    license = "BSD"
    url = "https://github.com/karasusan/conan-blosc"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = { "shared": [True, False]
              , "fPIC": [True, False]
              }
    default_options = "shared=False", "fPIC=True"
    exports = ["FindBlosc.cmake", "fix-shared-lib-install.patch"]

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.remove("fPIC")

    def configure(self):
        if self.options.shared and "fPIC" in self.options.fields:
            self.options.fPIC = True

    def source(self):
        self.run("git clone https://github.com/Blosc/c-blosc src")
        self.run("cd src && git checkout v%s" % self.version)
        self.run("cd src && git apply ../fix-shared-lib-install.patch")
        replace_in_file("src/CMakeLists.txt", "project(blosc)",
                        "project(blosc)\ninclude(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)\nconan_basic_setup()")

    def build(self):
        cmake = CMake(self)
        cmake.definitions.update(
            { "BUILD_SHARED": self.options.shared
            , "BUILD_STATIC": not self.options.shared
            , "BUILD_TESTS": False
            , "BUILD_BENCHMARKS": False
            , "PREFER_EXTERNAL_LZ4": False
            , "PREFER_EXTERNAL_SNAPPY": False
            , "PREFER_EXTERNAL_ZLIB": False
            , "PREFER_EXTERNAL_ZSTD": False
            , "CMAKE_INSTALL_PREFIX": self.package_folder
            })
        if "fPIC" in self.options.fields:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC

        cmake.configure(source_dir="src")
        cmake.build(target="install")

    def package(self):
        self.copy("FindBlosc.cmake", ".", ".")
        self.copy("*.txt", src="src/LICENSES", dst="licenses")

    def package_info(self):
        prefix = "lib" if self.settings.os == "Windows" and not self.options.shared else ""
        self.cpp_info.libs.append(prefix + "blosc")
        if self.settings.os == "Windows" and self.options.shared:
            self.cpp_info.defines.append("BLOSC_SHARED_LIBRARY")
