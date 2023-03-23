# @Author Abdelaziz Salah Mohammed
# this method is not valid, because the track is generic, so we can't depend on fixed points.
import cv2
import numpy as np


def showingImg(bounding_rectangle):
    cv2.imshow('Image_Rec', bounding_rectangle)
    cv2.waitKey(0)


def findBoundingRectangleArea(img, contours):
    # This function tries to fit the minimum bounding rectangle for the given contours.

    # [5] TODO: Find the minimum bounding rectangle that can fit the given contours.
    # Hint: Check the function boundingRect in opencv

    # TODO (Optional): You can uncomment the following lines to show or display the bounded rectangle.
    # x,y,w,h = cv2.boundingRect(contours[1])

    x, y, w, h = cv2.boundingRect(contours[11])
    bounding_rectangle = cv2.rectangle(
        img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    showingImg(bounding_rectangle)

    # drawing multiple points
    # # if bounding_rectangle: ## not none
    # showingImg(bounding_rectangle)

    # bounding_rectangle = cv2.rectangle(
    #     img, (x + w - 100, y), (x + w - 90, y + 10), (0, 255, 0), 2)

    # bounding_rectangle = cv2.rectangle(
    #     img, (x + 100, y), (x + 110, y + 10), (0, 255, 0), 2)

    # bounding_rectangle = cv2.rectangle(
    #     img, (x + w - 100, y + h), (x + w - 90, y + h - 20), (0, 255, 0), 2)

    # bounding_rectangle = cv2.rectangle(
    #     img, (x + 100, y + h), (x + 110, y + h - 20), (0, 255, 0), 2)

    # showingImg(bounding_rectangle)
    # # [6] TODO: Find the area of the bounding rectangle
    # area = w * h
    # return area, bounding_rectangle


# this will need to be dynamicly evaluated to get the image.
# we will not need to process the road every time, we will just need to process the image once.
img = cv2.imread('./TurnsDetection/realTrack.jpg', cv2.IMREAD_UNCHANGED)
# img = cv2.imread('./images/roads/road1.jpg', cv2.IMREAD_UNCHANGED)

# convert img to grey
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# set a thresh
thresh = 100
# get threshold image
ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
# find contours
contours, hierarchy = cv2.findContours(
    thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# drawing the contours
# cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
# cv2.imshow('Image', img)
# cv2.waitKey(0)

# create an empty image for contours
img_contours = np.zeros(img.shape)

findBoundingRectangleArea(img, contours)
