import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

print sys.argv



img = cv2.imread('/home/anoop/Workspace/Learn_OpenCV/data/images/cat_and_dog.jpg')

# If we don't exchange R,B channels, they are distorted in matplotlib.
# http://stackoverflow.com/questions/40067243/matplotlib-adding-blue-shade-to-an-image 
im2 = img.copy()
im2[:, :, 0] = img[:, :, 2]
im2[:, :, 2] = img[:, :, 0]

fig = plt.figure()
fig.suptitle('Image Histogram and channel splitting')


ax = plt.subplot(2, 3, 1)
ax.set_title("Original Image")
ax.imshow(im2)

ax = plt.subplot(2, 3, 2)
color = ('b','g','r')
for i,col in enumerate(color):
	histr = cv2.calcHist([im2],[i],None,[256],[0,256])
	plt.plot(histr,color = col)
	plt.xlim([0,256])
ax.set_title("R,G,B Histogram")

b,g,r = cv2.split(img)

ax=plt.subplot(2, 3, 4)
ax.set_title("Red Channel")
ax.imshow(r,"gray")

ax=plt.subplot(2, 3, 5)
ax.set_title("Green Channel")
ax.imshow(g, "gray")

ax=plt.subplot(2, 3, 6)
ax.set_title("Blue Channel")
ax.imshow(b, "gray")

plt.show()