import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
import os


file_name = os.path.join(os.path.dirname(__file__), '../data/images/cat_and_dog.jpg')

if len(sys.argv) > 1:
	file_name = sys.argv[1]


img = cv2.imread(file_name)

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