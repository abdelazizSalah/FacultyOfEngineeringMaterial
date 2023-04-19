import asyncio
import numpy as np
import websockets
import cv2
from lineDetection import *
from skimage.morphology import binary_erosion, binary_dilation, binary_closing, skeletonize, thin
import math
from skimage import io


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
        [1, 1, 1, ],
        [1, 1, 1, ],
        [1, 1, 1, ],
    ])

    # use erosion to remove thin lines and pixels (errors)
    img = binary_erosion(image=img, footprint=mask)

    # convert img to float
    img = np.float32(img)

    # Detect car Corners

    # TODO: 20 should be changed to be able to get only 4 points only
    # TODO: so to do this we should do a loop here, and change the value of 20, till the len on corners is 4
    # TODO: 4 should be 5 to avoid false positives.
    # parameters(Grayscale image, Maximum number of corners we want,Quality level parameter(preferred value=0.01),Maximum distance between points)
    for i in range(140, 150):
        corners = cv2.goodFeaturesToTrack(img, 5, 0.1, i)
        if len(corners) == 4:
            print(i)
            break

    # corners point
    points = []

    for corner in corners:
        # this returns x,y for each corner ponit
        x, y = corner.ravel()
        points.append(np.array([int(x), int(y)]))
        # Draw corner Points
        cv2.circle(img, (int(x), int(y)), 3, (255, 0, 0), -1)
        cv2.imshow('frame', img)

    return img


async def upload(websocket):

    async for message in websocket:
        nparr = np.frombuffer(message, np.uint8)
        nparr = nparr.reshape(240, 320)
        img = nparr.copy()

        # print(type(message))
        # print(nparr)
        img = detectingLines(nparr)
        # img = await detectCar(img)

        # convert the image to 3-channel format (if it is not already)
        # convert the numpy array to the source data type required for cv2.imshow
        src_data = cv2.cvtColor(
            (img * 255).astype(np.uint8), cv2.COLOR_GRAY2BGR)

        # displaying the frame with fps
        cv2.imshow('frame', src_data)

        # press 'Q' if you want to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


async def main():
    async with websockets.serve(upload, "192.168.42.151", 8765, ping_interval=None):
        await asyncio.Future()  # run forever

asyncio.run(main())
