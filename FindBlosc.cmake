set(BLOSC_INCLUDE_DIRS "${CONAN_INCLUDE_DIRS_BLOSC}")
set(BLOSC_LIBRARY_DIRS "${CONAN_LIB_DIRS_BLOSC}")
set(BLOSC_BINARY_DIRS  "${CONAN_BIN_DIRS_BLOSC}")

set(BLOSC_INCLUDE_DIR  "${BLOSC_INCLUDE_DIRS}")
set(BLOSC_LIBRARY_DIR  "${BLOSC_LIBRARY_DIRS}")
set(BLOSC_BINARY_DIR   "${BLOSC_BINARY_DIRS}")

conan_find_libraries_abs_path("${CONAN_LIBS_BLOSC}" "${BLOSC_LIBRARY_DIRS}" BLOSC_LIBRARIES)

foreach (INCLUDE_DIR ${BLOSC_INCLUDE_DIRS})
    if(NOT BLOSC_VERSION AND INCLUDE_DIR AND EXISTS "${INCLUDE_DIR}/blosc.h")
      file(STRINGS
           ${INCLUDE_DIR}/blosc.h
           TMP
           REGEX "#define BLOSC_VERSION_STRING.*$")
      string(REGEX MATCHALL "[0-9.]+" BLOSC_VERSION ${TMP})
    endif()
endforeach()

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(IlmBase
    REQUIRED_VARS
        BLOSC_INCLUDE_DIRS
        BLOSC_LIBRARIES
    VERSION_VAR
        BLOSC_VERSION
)
