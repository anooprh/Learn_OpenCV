### Building OpenCV 

Get the open source from github

`git clone git@github.com:Itseez/opencv.git`

`cd opencv`

`mkdir build`

`cmake ..`  for plain vanilla Open CV 
OR 
`cmake -D OPENCV_EXTRA_MODULES_PATH=<path/to/opencv_contrib/modules@https://github.com/opencv/opencv_contrib/tree/master/modules>` for additional functionality

`make`

`sudo make install`


Now OpenCV is built and installed on your system.

It can be used in other programs

i.e `${OpenCV_LIBS}` and `find_package( OpenCV REQUIRED )` will be automatically in cmake files for other projects (read application projects)
`#include <opencv2/opencv.hpp>` will work in your .cpp files

Recomended approach to use openCV is to use it with Cmake build system, rather than manually trying to link with the library(Will probably try that soon as well)

### Setting up Python version of OpenCV

Install virtual env system wide if not installed previously
`sudo pip install virtualenv` works most of the time

Create a virtual env
`virtualenv new opencv_python`

Install the dependencies
`pip install -r requirements.txt`

OpenCV can't be installed this way
Copy cv2.so from previous step into "opencv_python/lib/python2.7/site-packages/" directory

Ocassionall save the requirements , `pip freeze > requirements.txt`