cmake_minimum_required(VERSION 3.12)

project(marty_pybinding)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG REQUIRED)

set(ALL_SOURCES
    simple_py.cpp
)

pybind11_add_module(pymartyc ${ALL_SOURCES})
target_link_libraries(pymartyc PRIVATE marty)