# @Description: ORB.py
# @Author: 孤烟逐云zjy
# @Date: 2020/5/3 11:39
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./images/photo01.jpg', 0)

# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# kp, des = orb.detectAndCompute(img, None)

# draw only keypoints location,not size and orientation
img = cv2.drawKeypoints(img,kp, None, color=(0,255,0), flags=0)
plt.imshow(img),plt.show()