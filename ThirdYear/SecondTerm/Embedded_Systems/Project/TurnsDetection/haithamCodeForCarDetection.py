import cv2
import numpy as np
from skimage.morphology import binary_erosion, binary_dilation, binary_closing, skeletonize, thin
import matplotlib.pyplot as plt
import math


def calcDsit(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)


def lineEq(p1, p2):
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p1[1] - m*p1[0]
    return m, c


# Read img and convert it to gray scale
img = cv2.imread('test.png')
img = img[:, :, :3]
# take copy of img
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# convert to gray scale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Sperate car from background
# change threshold to sperate correctly
img[(img < 15) | (img > 240)] = 0

img[(img > 15) & (img < 240)] = 1

# mask that used in erosion
mask = np.array([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
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
corners = cv2.goodFeaturesToTrack(img, 4, 0.1, 20)

# corners point
points = []

for corner in corners:
   # this returns x,y for each corner ponit
    x, y = corner.ravel()
    points.append(np.array([int(x), int(y)]))
    # Draw corner Points
    cv2.circle(img, (int(x), int(y)), 3, 255, -1)

# This code get the forward point
# the width larger than hight so we get the closed two pairs of points and get midpoint for each pair
# forward point shold have gray scale value higher than the backward point
####################################################################################################
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
# define the forward point at the line which has higher brightness.               (x,y)
if(imggray[midpoints[0][1]][midpoints[0][0]] < imggray[midpoints[1][1]][midpoints[1][0]]):
    forwardPoint = midpoints[1]
else:
    forwardPoint = midpoints[0]
# Draw mid point
cv2.circle(img, (forwardPoint[0], forwardPoint[1]), 3, 255, -1)
####################################################################################################

# Get line Equation used to detect if line or curve
m, c = lineEq(midpoints[0], midpoints[1])
curve = 0

# this code detect the direction of the car
# bnrg3 sena wara 34an ne3rf ehna el direction bta3 el 3arabya.
####################################################################################################
y = (forwardPoint[0] - (minmumDistance//4)) * m + c
y_range = imggray[int(round(y) - (minmumDistance//6)): int(round(y) +
                                                           (minmumDistance//6)), int(forwardPoint[0] - (minmumDistance//4))]
# el factor da bsta5demo eny 3awz el3arabya tshof 2damha 2ad eh mn el eswed w hya bt7ded ely 2damha line wla curve lw ghyato el5t ely tale3 mn el3rabya hytghyer
# TODO: to be changed till you can get the best length and result.
factor = 2.5
if ((y_range < 50).astype(bool).any()):
    minX = forwardPoint[0] - int(minmumDistance * factor)
    maxX = forwardPoint[0] - 5
else:
    minX = forwardPoint[0] + 5
    maxX = forwardPoint[0] + int(minmumDistance * factor)
####################################################################################################

# msh ba5od el y blzabt ba5od range 3lashan el3rabya msh 3la el line blzabt (error) w momkn tghyer el range
yRange = minmumDistance//4
print(minX, maxX)
for i in range(minX, maxX):
    y = i * m + c
    y_range = imggray[int(round(y) - (yRange)): int(round(y) + (yRange)), i]
    # check law mafesh eswd ya3ny el line msh kamel (curve)
    if ~(y_range < 50).astype(bool).any():
        curve = 1
# barsem el line ely 2dam el3rabya msh 2kter
for i in range(minX, maxX):
    y = i * m + c
    cv2.circle(imggray, (i, int(y)), 3, 0, -1)

if curve == 1:
    print('Curve')
else:
    print('Straight Line')

plt.imshow(imggray, cmap='gray')
plt.show()
plt.imshow(img, cmap='gray')
plt.show()
