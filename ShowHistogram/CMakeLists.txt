cmake_minimum_required(VERSION 2.8)
project( ShowHistogram )
find_package( OpenCV REQUIRED )
add_executable( ShowHistogram ShowHistogram.cpp )
target_link_libraries( ShowHistogram ${OpenCV_LIBS})
