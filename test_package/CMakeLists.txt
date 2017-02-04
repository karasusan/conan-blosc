PROJECT(PackageTest)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

find_package(Blosc REQUIRED)

ADD_EXECUTABLE(testPackage main.cpp)
include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${BLOSC_INCLUDE_DIRS})
TARGET_LINK_LIBRARIES(testPackage ${BLOSC_LIBRARIES})
