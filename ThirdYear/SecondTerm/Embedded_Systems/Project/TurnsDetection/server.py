import asyncio
import numpy as np
import websockets
import cv2
from lineDetection import *
from skimage.morphology import binary_erosion, binary_dilation, binary_closing, skeletonize, thin
import math


def calcDsit(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)


def lineEq(p1, p2):
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p1[1] - m*p1[0]
    return m, c


async def detectCar(img):

    # applying segmentation, to segment all black and white background as black, and the color of the car as white
    img[(img < 50) | (img > 150)] = 0
    img[(img > 50) & (img < 150)] = 255

    # # mask that used in erosion
    mask = np.array([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ])

    # use erosion to remove thin lines and pixels (errors)
    # img = binary_erosion(image=img, footprint=mask)

    return img


async def upload(websocket):

    async for message in websocket:
        nparr = np.frombuffer(message, np.uint8)
        nparr = nparr.reshape(240, 320)
        img = nparr.copy()

        # print(type(message))
        # print(nparr)
        # img = detectingLines(nparr)
        img = await detectCar(img)

        # displaying the frame with fps
        cv2.imshow('frame', img)

        # press 'Q' if you want to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


async def main():
    async with websockets.serve(upload, "192.168.43.58", 8765, ping_interval=None):
        await asyncio.Future()  # run forever

asyncio.run(main())
