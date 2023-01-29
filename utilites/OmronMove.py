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
            z += 1
            print("up")

         if keyboard.is_pressed('a'):
            y += 1
            print("left")

         if keyboard.is_pressed('s'):
            z -= 1
            print("down")

         if keyboard.is_pressed('d'):
            y -= 1
            print("right")
         await conn.move_to_point_ptp([x, y, z, 178, -0.2, -90], 1, 200)



asyncio.run(move())




