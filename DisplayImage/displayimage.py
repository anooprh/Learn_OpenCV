# import the necessary packages
import numpy as np
import cv2
 
# load the games image
image = cv2.imread("/home/anoop/Workspace/Learn_OpenCV/data/images/cat_and_dog.jpg")
cv2.imshow('image',image) # Display the picture
cv2.waitKey(0) # wait for closing
cv2.destroyAllWindows() # Ok, destroy the window