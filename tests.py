import numpy as np
import cv2
import os
import sys
from uarm.wrapper import SwiftAPI
from uarm.utils.log import logger
import keyboard
import mediapipe as mp
import imutils
from time import sleep

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

MIN_MATCH_COUNT = 10


logger.setLevel(logger.VERBOSE)

swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'}, callback_thread_pool_size=1)
swift.waiting_ready()

device_info = swift.get_device_info()
print(device_info)

sleep(5)
print(swift.get_polar())

swift.set_speed_factor(factor=10)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pos = {}

#startpositions
x = 180
z = 100
y = 20

n = 0

def draw_hand_connections(img, results):
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape

                # Finding the coordinates of each landmark
                cx, cy = int(lm.x * w), int(lm.y * h)

                # Printing each landmark ID and coordinates
                # on the terminal
                #print(id, cx, cy)

                pos[id] = [cx, cy]

                # Creating a circle around each landmark
                cv2.circle(img, (cx, cy), 10, (0, 255, 0),
                cv2.FILLED)
                # Drawing the landmark connections
                mpDraw.draw_landmarks(img, handLms,
                mpHands.HAND_CONNECTIONS)
    return img

def getmid(l):
    y = l[0]
    z = l[1]
    print("1", y, z)
    y = (y / 500 - 1) / -1 * 360 - 180
    z = (z / 500 - 1) / -1 * 140 + 20
    print("2", y, z)
    swift.set_position(x, y ,z)

def posisjons():
    global n, pos
    if pos != {}:
        eight = pos.get(8)[1]
        for x in range(21):
            if x != 8:
                if pos.get(x)[1] < eight:
                    break
        else:
            n += 1
            print("is", n)
            getmid(pos.get(8))
    pos = {}

def main():
    while True:
        succes, img = cap.read()
        if succes:
            img = imutils.resize(img, width=500, height=500)

            results = hands.process(img)
            draw_hand_connections(img, results)
            posisjons()
            cv2.imshow("ogmm", img)
            cv2.waitKey(1)


if __name__ == "__main__":
    main()

