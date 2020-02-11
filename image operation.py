import numpy as np
import cv2

img = cv2.imread('watch.jpg', 1)       # cv2.IMREAD_COLOR


# a white box or to chnge the value of pixels for the portion of image
img[55, 55] = [255, 255, 255]
px = img[55, 55]

img[100:150, 100:150] = [255, 255, 255]

#making a copy of a certain part of image
watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face


#to show
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
