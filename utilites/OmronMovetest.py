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