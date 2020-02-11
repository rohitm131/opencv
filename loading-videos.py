import cv2
import numpy as np

#to access video from webcam
cap = cv2.VideoCapture(0)

#to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #converting into grayscale
    #out.write(frame)     to save the output
    
    
    cv2.imshow('frame', frame)       #output
    cv2.imshow('gray', gray)        #ouput in grayscale

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
