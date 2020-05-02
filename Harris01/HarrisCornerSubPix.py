# @Description: HarrisCornerSubPix.py
# @Author: 孤烟逐云zjy
# @Date: 2020/5/2 12:41
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/


import cv2 as cv
import numpy as np


image = cv.imread("./images/photo01.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2,3,0.04)
dst = cv.dilate(dst, None)
ret, dst = cv.threshold(dst, 0.01*dst.max(), 255,0)
dst = np.uint8(dst)

ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv.cornerSubPix(gray, np.float32(centroids), (5,5),(-1,-1),criteria)

res = np.hstack((centroids, corners))
res = np.int0(res)
image[res[:,1],res[:,0]]=[0,0,255]
image[res[:,3],res[:,2]]=[0,255,0]
cv.imshow("subpix", image)

cv.waitKey(0)
cv.destroyAllWindows()