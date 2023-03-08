import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from uarm.wrapper import SwiftAPI
from uarm.utils.log import logger
import keyboard
import mediapipe as mp
import imutils

logger.setLevel(logger.VERBOSE)


swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'}, callback_thread_pool_size=1)
swift.waiting_ready()


device_info = swift.get_device_info()
print(device_info)

time.sleep(5)
print(swift.get_polar())


swift.set_speed_factor(factor=1)

x = 100
y = 0
z = 0

def test(ret):
    print(ret)


while True:
    if keyboard.is_pressed('w'):
        while keyboard.is_pressed('w'):
            pass
        x += 20
        swift.set_position(x, y, z)

    elif keyboard.is_pressed('s'):
        while keyboard.is_pressed('s'):
            pass
        x -= 20
        swift.set_position(x, y, z)

    if keyboard.is_pressed('a'):
        while keyboard.is_pressed('a'):
            pass
        z += 20
        swift.set_position(x, y, z)

    elif keyboard.is_pressed('d'):
        while keyboard.is_pressed('d'):
            pass
        z -= 20
        swift.set_position(x, y, z)

    if keyboard.is_pressed('q'):
        while keyboard.is_pressed('q'):
            pass
        y += 20
        swift.set_position(x, y, z)


    elif keyboard.is_pressed('e'):
        while keyboard.is_pressed('e'):
            pass
        y -= 20
        swift.set_position(x, y, z)

    print("x = ", x, "y = ", y, "z = ", z)





