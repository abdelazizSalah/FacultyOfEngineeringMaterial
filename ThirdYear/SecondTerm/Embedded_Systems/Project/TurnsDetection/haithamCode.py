import asyncio
import numpy as np
import websockets
import cv2
import math
from skimage.morphology import binary_erosion, binary_dilation, binary_closing, skeletonize, thin


def calcDsit(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)


def lineEq(p1, p2):
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p1[1] - m*p1[0]
    return m, c


def detectCar(img):
    imggray = img
    img[(img < 15) | (img > 240)] = 0

    img[(img > 15) & (img < 240)] = 1

    mask = np.array([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ])

    img = binary_erosion(image=img, footprint=mask)
    # img = binary_erosion(image=img,footprint=mask)
    # img = binary_dilation(image=img,footprint=mask)
    # img = binary_dilation(image=img,footprint=mask)

    img = np.float32(img)

    corners = cv2.goodFeaturesToTrack(img, 4, 0.1, 20)
    corners = np.int0(corners)

    points = []
    x_2 = []
    y_1 = []
    y_2 = []

    for corner in corners:
        points.append(corner.ravel())
        x, y = corner.ravel()

        cv2.circle(img, (x, y), 3, 255, -1)

    # print(np.array(points))

    minDist = 0
    pointPairIndex = []

    min1 = calcDsit(points[0], points[1])
    min2 = calcDsit(points[0], points[2])
    min3 = calcDsit(points[0], points[3])

    minmumDistance = 0

    if min1 < min2:
        if min1 < min3:
            pointPairIndex.append([0, 1])
            pointPairIndex.append([2, 3])
            minmumDistance = min1
        else:
            pointPairIndex.append([0, 3])
            pointPairIndex.append([1, 2])
            minmumDistance = min3
    else:
        if min2 < min3:
            pointPairIndex.append([0, 2])
            pointPairIndex.append([1, 3])
            minmumDistance = min2
        else:
            pointPairIndex.append([0, 3])
            pointPairIndex.append([1, 2])
            minmumDistance = min3

    pointPairIndex = np.array(pointPairIndex)

    midpoints = []

    mid1 = (points[pointPairIndex[0][0]] + points[pointPairIndex[0][1]]) // 2
    mid2 = (points[pointPairIndex[1][0]] + points[pointPairIndex[1][1]]) // 2

    midpoints = np.array([mid1, mid2])

    forwardPoint = 0

    if(imggray[midpoints[0][1]][midpoints[0][0]] < imggray[midpoints[1][1]][midpoints[1][0]]):
        forwardPoint = midpoints[1]
    else:
        forwardPoint = midpoints[0]

    # threshold = 20
    # visited = np.zeros(len(TrackPoints))

    # for i in range(len(TrackPoints)):
    #     d = calcDsit(forwardPoint,TrackPoints[i])
    #     # cv2.circle(img,(TrackPoints[i][0] ,TrackPoints[i][1]),3,255,-1)

    #     if d < threshold:
    #         if visited[i] == 0:
    #             visited[i] = 1
    #             # TODO: here we should send a slow signal or toggle space.
    #             print(TrackPoints[i])
    #             # print('slow')

    print(forwardPoint)

    cv2.circle(img, (forwardPoint[0], forwardPoint[1]), 3, 255, -1)
    return img


async def upload(websocket):

    async for message in websocket:
        nparr = np.frombuffer(message, np.uint8)
        nparr = nparr.reshape(240, 320)
        # print(type(message))
        print(nparr)
        # displaying the frame with fps
        img = detectCar(nparr)
        cv2.imshow('frame', img)

        # press 'Q' if you want to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


async def main():
    async with websockets.serve(upload, "192.168.43.58", 8765, ping_interval=None):
        await asyncio.Future()  # run forever

asyncio.run(main())
