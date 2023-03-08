import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from time import sleep
import asyncio
import techmanpy
MIN_MATCH_COUNT = 10wwwwwdaaaaaaaaaaaaaaaaaaaaaaadddddddaweeeeeeeeeqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqeeeeeeeee
img1 = cv.imread('test pictures/box test.png',0)          # queryImage
# Initiate SIFT detector
sift = cv.SIFT_create()
cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
kp1, des1 = sift.detectAndCompute(img1, None)
FLANN_INDEX_KDTREE = 1

cv.waitKey(0)
def getmid(l):
    y = 0
    z = 0
    for m in range(4):
        y += l[m][0][0]
        z += l[m][0][1]
    print("1", y, z)
    y = (y / 4 / 640 - 1) / -1 * 800 - 400
    z = (z / 4 / 480 - 1) / -1 * 940 - 240
    print("2", y, z)
    return y, z


x = -500
y = 0
z = 500
while True:
    succes, img = cap.read()
    if succes:
        img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        kp2, des2 = sift.detectAndCompute(img2, None)

        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        flann = cv.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1, des2, k=2)

        good = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append(m)
        if len(good) > MIN_MATCH_COUNT:
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
            M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
            h, w = img1.shape
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            dst = cv.perspectiveTransform(pts, M)
            img2 = cv.polylines(img2, [np.int32(dst)], True, 255, 3, cv.LINE_AA)
            y, z = getmid(dst)
        else:
            print("Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))

        plt.imshow(img2, 'gray'), plt.show()
        sleep(1)
        plt.close()

