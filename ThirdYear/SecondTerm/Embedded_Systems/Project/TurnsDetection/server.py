import asyncio
import numpy as np
import websockets
import cv2
from lineDetection import *


async def upload(websocket):

    async for message in websocket:
        nparr = np.frombuffer(message, np.uint8)
        nparr = nparr.reshape(240, 320)
        # print(type(message))
        # print(nparr)
        img = detectingLines(nparr)

        # displaying the frame with fps
        cv2.imshow('frame', img)

        # press 'Q' if you want to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


async def main():
    async with websockets.serve(upload, "192.168.43.58", 8765, ping_interval=None):
        await asyncio.Future()  # run forever

asyncio.run(main())
