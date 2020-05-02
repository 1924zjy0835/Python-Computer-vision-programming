# @Description: Shi-Tomasi.py
# @Author: 孤烟逐云zjy
# @Date: 2020/5/2 12:52
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("./images/photo01.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# gray = cv.Canny(img, 200, 300)
corners = cv.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y),3, 255, -1)

plt.imshow(img)
plt.show()