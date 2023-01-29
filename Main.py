import cv2 as cv
import numpy as np

print("initialization")

kernel = np.ones((5,5),np.uint8)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

print("running")



while True:
    success, img = cap.read()
    img = cv.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv.GaussianBlur(img, (7, 7), 0)
    img = cv.Canny(img, 100, 100)
    img = cv.dilate(img, kernel, iterations=1)
    img = cv.erode(img, kernel, iterations=1)
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break

