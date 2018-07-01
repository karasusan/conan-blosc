project(PackageTest)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
set(CMAKE_SKIP_RPATH 0)

find_package(Blosc REQUIRED)

add_executable(testPackage main.cpp)
include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${BLOSC_INCLUDE_DIRS})
target_link_libraries(testPackage ${CONAN_LIBS})
