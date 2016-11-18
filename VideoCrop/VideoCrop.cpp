#include <iostream>
#include <opencv2/opencv.hpp>

int main() {
    // Open the first camera attached to your computer
    cv::VideoCapture cap(0);
    if(!cap.isOpened()) {
        std::cout << "Unable to open the camera" << std::endl;
        std::exit(-1);
    }
 
    cv::Mat image;
    double FPS = 24.0;
    // Read camera frames (at approx 24 FPS) and show the result

    int width = static_cast<int>(cap.get(CV_CAP_PROP_FRAME_WIDTH));
    int height = static_cast<int>(cap.get(CV_CAP_PROP_FRAME_HEIGHT));
    int radius = std::min(width, height)/2;
    std::cout << "Width  : " << width << ", " << 
                 "Height : " << height << ", " << 
                 "Radius : " << radius << ", " <<
                 std::endl;
    cv::Point center(width/2, height/2);

    while(true) {
        cap >> image;
        cv::Mat mask(image.size(),image.type());
        mask.setTo(cv::Scalar(255,255,255));
        circle(mask, center, radius, cv::Scalar(0,0,0), -1, 8, 0);
        cv::bitwise_or(mask,image,image);
        if(image.empty()) {
            std::cout << "Can't read frames from your camera" << std::endl;
            break;
        }

        cv::imshow("Camera feed", image);

        if(cv::waitKey(1000.0/FPS) == 27) break;
    }
 
    return 0;
}