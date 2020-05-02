# @Description: SIFT.py
# @Author: 孤烟逐云zjy
# @Date: 2020/5/2 13:02
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./images/photo01.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# opencv将SIFT()算法整合到xfeatures2d集合里面了
# sift = cv.SFIT()
sift = cv.xfeatures2d.SIFT_create()

kp = sift.detect(gray, None)
img = cv.drawKeypoints(gray, kp, img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow("sift_images", img)

cv.waitKey(0)
cv.destroyAllWindows()

