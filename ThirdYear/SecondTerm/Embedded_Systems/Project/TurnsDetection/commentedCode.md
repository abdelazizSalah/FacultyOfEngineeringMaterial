

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
