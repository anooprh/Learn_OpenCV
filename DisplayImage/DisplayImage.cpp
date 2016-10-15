#include <stdio.h>
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;

int main(int argc, char** argv ){
    if ( argc != 2 ){
        cout << "usage: DisplayImage.out <Image_Path>" << endl;
        return -1;
    }

    cv::Mat image;
    image = cv::imread( argv[1]);
    cout << "Image size : width=" << image.size().width << " ,height=" << image.size().height << endl;

    if ( !image.data ){
        cerr << "No image data" << endl;;
        return -1;
    }
    cv::namedWindow("Display Image", cv::WINDOW_AUTOSIZE );
    cv::imshow("Display Image", image);

    cv::waitKey(0);

    return 0;
}
