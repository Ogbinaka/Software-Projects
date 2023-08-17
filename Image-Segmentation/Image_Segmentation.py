#I used jupyter Notebook as my code editor

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#import the image file e.g Map of New Jersey
image = cv.imread('Map_Of_NJ.jpg')

# OpenCV intepretes things differently (it swaps the color formation). We have to standardized the color to produce a more accurate result.
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

#This turns the image into Black and White
gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

#Converts all color pixels to "0's" and "1's" or binary

#In this case, outside the map of NJ is labelled as '0' within the map is labelled as '1'
_, binary = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)

label_image = np.where(binary == 0, 0, 1)

#plot the image of the picture in a x, y axis. This is optional and merely used as a visualizer
plt.imshow(gray, cmap="gray")

#This is to verify that the pixels to binary conversion works. So I exported the binary image to csv file, and I could see some 1's in the rows (row ~19271 to be precise)

img = np.array(label_image)

img_flat = img.flatten()

save_img = np.savetxt('image.csv', img_flat, delimiter=',')

save_img


#This is an optional step and used if you want to draw the edges or contour of the map
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

image = cv.drawContours(image, contours, -1, (0, 255, 0), 3)

plt.imshow(image)
