# @Description: setMouseCallback.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/27 8:49
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

# 安装opencv-python
import cv2 as cv
import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i]
# print(events)


def onMouseAction(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("左键点击")
    elif event == cv.EVENT_RBUTTONDOWN:
        print("右键点击")
    elif flags == cv.EVENT_FLAG_LBUTTON:
        print("左键拖曳")
    elif event == cv.EVENT_MBUTTONDOWN:
        print("中键点击")


def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 100, (255, 0,0), -1)
        print("左键点击")


img = np.zeros((500, 500, 3), np.uint8)
cv.namedWindow("image")
cv.setMouseCallback("image", draw_circle)

while(1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()
