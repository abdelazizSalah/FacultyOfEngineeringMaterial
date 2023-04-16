# ################################################################
# Program made to detect lines and from them we can detect curves
# We store the points in order to detect the curves and make the car
# move slowly when it meets a curve
# @ Author Abdelaziz Salah.
# ###############################################################
'''
    Important Notes:
        1. the image starts from the top left corner, so the (0,0) point is the top left corner
        2. we can sort them by using x1, y1, so we get them in order of the most left and upper points.
'''
import cv2
import numpy as np
import functools


def compare(item1, item2):
    '''
        utility function used to sort the lines by the x1 value
        and if they were equal in x, we sort them by y1 value
        in an ascending order
    '''
    if item1[0] < item2[0]:
        return -1
    elif item1[0] > item2[0]:
        return 1
    else:
        if item1[1] < item2[1]:
            return -1
        elif item1[1] > item2[1]:
            return 1
        else:
            return 0


def skin_detector_hsv(bgr_image):
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
    skin_region = cv2.inRange(hsv_image, (0, 0, 0), (20, 20, 20))
    return skin_region


def apply_skin_detector(img):
    detected_skin = skin_detector_hsv(img)
    bgr = cv2.cvtColor(detected_skin, cv2.COLOR_GRAY2BGR)
    bgr = cv2.erode(bgr, np.ones((12, 12), np.uint8))
    bgr = cv2.dilate(bgr, np.ones((35, 35), np.uint8))
    bgr = cv2.erode(bgr, np.ones((15, 15), np.uint8))
    # boxes = find_contours(bgr)
    return boxes


def detectingLines(gray):
    # # Reading the required image in
    # # which operations are to be done.
    # # Make sure that the image is in the same
    # # directory in which this python program is
    # img = cv2.imread('realTrack.jpg')

    # # Convert the img to grayscale
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply edge detection method on the image
    # edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    edges = cv2.Canny(gray, 50, 150)

    # This returns an array of r and theta values
    # lines = cv2.HoughLinesP(edges, 1, np.pi/180, 200)
    lines = cv2.HoughLinesP(
        edges,  # Input edge image
        1,  # Distance resolution in pixels
        np.pi/180,  # Angle resolution in radians
        threshold=70,  # Min number of votes for valid line
        minLineLength=50,  # Min allowed length of line -> a2al length l ay line
        maxLineGap=40  # Max allowed gap between line for joining them -> a2al gab ben el lines to be considered new
    )

    # Calling
    lines = sorted(lines[:, 0], key=functools.cmp_to_key(compare))

    # iterating over each line and draw it.
    for points in lines:
        x1, y1, x2, y2 = points
        # this condition for removing the lines that are not in the track
        if(x1 < 20 or x2 < 20 or x1 > 1150 or x2 > 1150):
            continue
        cv2.line(gray, (x1, y1), (x2, y2), (0, 0, 250), thickness=5)

    # All the changes made in the input image are finally
    # written on a new image houghlines.jpg
    return gray
