



kernel = np.ones((15, 15), np.float32)/255
smoothed = cv2.filter2D(res, -1, kernel)

blur = cv2.GaussianBlur(res, (15, 15), 0)
median_blur = cv2.medianBlur(res, 15)
bilateral_blur = cv2.bilateralFilter(res, 15, 75, 75)
