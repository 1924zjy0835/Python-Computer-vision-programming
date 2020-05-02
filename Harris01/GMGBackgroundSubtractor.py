# @Description: GMGBackgroundSubtractor.py
# @Author: 孤烟逐云zjy
# @Date: 2020/5/2 12:14
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import numpy as np
import cv2 as cv


kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
fgbg = cv.createBackgroundSubtractorKNN()

while(1):
    image = cv.imread("./images/photo01.jpg")
    fgmask = fgbg.apply(image)
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_ELLIPSE, kernel)
    cv.imshow("frame", fgmask)

    k = cv.waitKey(0) & 0xff
    if k == 27:
        break

cv.destroyAllWindows()
