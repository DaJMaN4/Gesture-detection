import asyncio
import techmanpy
import keyboard
from time import sleep

async def move():
   async with techmanpy.connect_sct(robot_ip='192.168.0.41') as conn:
      x = -500
      y = 0
      z = 500
      while True:
         if keyboard.is_pressed('w'):
            while keyboard.is_pressed('w'):
               pass
            z += 10
            print("up")

         if keyboard.is_pressed('a'):
            while keyboard.is_pressed('a'):
               pass
            y += 10
            print("left")

         if keyboard.is_pressed('s'):
            while keyboard.is_pressed('s'):
               pass
            z -= 10
            print("down")

         if keyboard.is_pressed('d'):
            while keyboard.is_pressed('d'):
               pass
            y -= 10
            print("right")

         await conn.move_to_point_ptp([x, y, z, 178, -0.2, -90], 1, 150)


asyncio.run(move())




#await conn.move_to_joint_angles_ptp([10, -10, 10, -10, 10, -10], 0.10, 200)


async def move():
   async with techmanpy.connect_sct(robot_ip='192.168.0.41') as conn:
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

                await conn.move_to_point_ptp([x, y, z, 178, -0.2, -90], 1, 150)
                plt.imshow(img2, 'gray'), plt.show()
                sleep(1)
                plt.close()