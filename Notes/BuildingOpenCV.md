Get the open source from github

$ git clone git@github.com:Itseez/opencv.git

$ cd opencv

$ mkdir build

$ cmake ..

$ make

$ sudo make install


Now OpenCV is built and installed on your system.

It can be used in other programs

i.e `${OpenCV_LIBS}` and `find_package( OpenCV REQUIRED )` will be automatically in cmake files for other projects (read application projects)
`#include <opencv2/opencv.hpp>` will work in your .cpp files

Recomended approach to use openCV is to use it with Cmake build system, rather than manually trying to link with the library(Will probably try that soon as well)
