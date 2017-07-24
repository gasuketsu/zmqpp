project(ConanZmqppTest CXX)
cmake_minimum_required(VERSION 2.8.12)

# prepare C++11
set(CMAKE_CXX_FLAGS "-std=c++11 ${CMAKE_CXX_FLAGS}")
# show all warnings
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -pedantic")
# Set compiler flags that don't work on Windows

if(NOT MSVC)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wextra")
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${CMAKE_PROJECT_NAME} test_main.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})
