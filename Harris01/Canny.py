# @Description: Canny.py
# @Author: 孤烟逐云zjy
# @Date: 2020/5/1 15:31
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2 as cv
import numpy as np

img = cv.imread("./images/photo01.jpg")
cv.imwrite("canny.jpg", cv.Canny(img, 200, 300))
cv.imshow("canny", cv.imread("canny.jpg"))
cv.waitKey(0)
cv.destroyAllWindows()
