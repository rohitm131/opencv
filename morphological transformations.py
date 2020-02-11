



kernel = np.ones((5, 5), np.unit8)
erosion = cv2.erode(mask, kernel, iterations = 1)
dilation = cv2.dilate(mask, kernel, iterations = 1)


opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


#It is the difference between input image and Opening of the image
cv2.imshow('Tophat', tophat)

#It is the difference between closing of the input image and input image
cv2.imshow('Blackhat', blackhat)
