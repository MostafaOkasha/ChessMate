import numpy as np
import cv2
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6 * 7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

images = glob.glob('/Users/robing/Documents/Projects/GitHub/OpenCVChess/IRS/pictures/sample_states/*.jpg')
#images = ["/Users/robing/Desktop/test.jpg"]

print(images)

# print(images)
for fname in images:

    # board_size = (7, 7)
    # img = cv2.imread(fname)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # # Find the chess board corners
    # ret, corners = cv2.findChessboardCorners(gray, board_size, flags=cv2.CALIB_CB_NORMALIZE_IMAGE | cv2.CALIB_CB_ADAPTIVE_THRESH)

    img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    imgr = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow('img', imgr)
    cv2.waitKey(0)

    board_size = (7, 7)
    ret, corners = cv2.findChessboardCorners(img, board_size, flags=cv2.CALIB_CB_NORMALIZE_IMAGE | cv2.CALIB_CB_NORMALIZE_IMAGE | cv2.CALIB_CB_FILTER_QUADS)
    print(ret, corners)
    # If found, add object points, image points (after refining them)
# if ret == True:
# objpoints.append(objp)
##
# corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
# imgpoints.append(corners2)
##
# Draw and display the corners
# img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
# cv2.imshow('img',img)
# cv2.waitKey(500)

cv2.destroyAllWindows()
