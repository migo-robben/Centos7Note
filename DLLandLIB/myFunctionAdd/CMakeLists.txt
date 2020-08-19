cmake_minimum_required(VERSION 3.16)
project(JustForTest)

set(CMAKE_CXX_STANDARD 11)

add_definitions(-DBUILDING_DLL)

add_subdirectory(lib)

add_executable(JustForTest main.cpp)
target_include_directories(JustForTest PUBLIC lib)
target_link_libraries(JustForTest myFunctionLib)