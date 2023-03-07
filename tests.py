import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
MIN_MATCH_COUNT = 10
img1 = cv.imread('test pictures/hand.jpg',0)

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

sift = cv.SIFT_create()
FLANN_INDEX_KDTREE = 1

while True:
    succes, img = cap.read()
    img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # BFMatcher with default params
    bf = cv.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])
    # cv.drawMatchesKnn expects list of lists as matches.
    img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    plt.imshow(img3), plt.show()


    x = 0
    y = 0
    for m in l:
        x += m[0]
        y += m[1]
    x /= 4
    y /= 4
    print(x, y)
