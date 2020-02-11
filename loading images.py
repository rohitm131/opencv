import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("watch.jpg",cv2.IMREAD_GRAYSCALE)
#IMREAD_GRAYSCALE = 0
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plotting using matplotlib
#plt.imshow(img, cmap='gray', interpolation='bicubic')

# drawing a line in the image
#plt.plot([50, 100], [80, 100], 'c', linewidth=5)

#showing image
#plt.show()

#saving image
cv2.imwrite('watchgray.png', img)
