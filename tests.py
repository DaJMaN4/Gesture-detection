import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (7, 7), 0)
    img = cv2.Canny(img, 100, 100)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break