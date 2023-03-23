# ################################################################
# # Example
# # Python program to illustrate HoughLine
# # method for line detection
import cv2
import numpy as np

# # Reading the required image in
# # which operations are to be done.
# # Make sure that the image is in the same
# # directory in which this python program is
img = cv2.imread('./TurnsDetection/realTrack.jpg')

# Convert the img to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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

print(lines)

# Printing
for points in lines:
    x1, y1, x2, y2 = points[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 250), thickness=5)

# The below for loop runs till r and theta values
# are in the range of the 2d array
# for r_theta in lines:
#     # drawing rectangles at the begining of the lines and the end

#     arr = np.array(r_theta[0], dtype=np.float64)
#     r, theta = arr
#     # Stores the value of cos(theta) in a
#     a = np.cos(theta)

#     # Stores the value of sin(theta) in b
#     b = np.sin(theta)

#     # x0 stores the value rcos(theta)
#     x0 = a*r

#     # y0 stores the value rsin(theta)
#     y0 = b*r

#     # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
#     x1 = int(x0 + 1000*(-b))

#     # # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
#     y1 = int(y0 + 1000*(a))
#     # print(x0, y0, sep=' , ')
#     # boundedRectange = cv2.rectangle(
#     #     img, (x0, y0), (x0 + 100, y0+100), (0, 0, 255), 2)

#     # # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
#     x2 = int(x0 - 1000*(-b))

#     # # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
#     y2 = int(y0 - 1000*(a))

#     # # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
#     # # (0,0,255) denotes the colour of the line to be
#     # # drawn. In this case, it is red.
#     cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# All the changes made in the input image are finally
# written on a new image houghlines.jpg
cv2.imwrite('linesDetected.jpg', img)
# 3
# Sabry
# 3
