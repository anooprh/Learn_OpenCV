#include <stdio.h>
#include <opencv2/opencv.hpp>

int main(int argc, char** argv ){
    if ( argc != 2 ){
        printf("usage: ConvToGrayScale <Image_Path>\n");
        return -1;
    }

    char* imageName = argv[1];
    cv::Mat image;
    image = cv::imread( imageName, 1 );

    if ( !image.data ){
        printf("No image data \n");
        return -1;
    }
    cv::Mat gray_image;
    cv::cvtColor( image, gray_image, CV_BGR2GRAY );

    cv::namedWindow( imageName, CV_WINDOW_AUTOSIZE );
    cv::namedWindow( "Gray image", CV_WINDOW_AUTOSIZE );

    cv::imshow( imageName, image );
    cv::imshow( "Gray image", gray_image );
    cv::waitKey(0);

    return 0;
}
