# @Description: createImage.py
# @Author: 孤烟逐云zjy
# @Date: 2020/5/3 9:49
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/


import cv2 as cv

im = cv.LoadImage('./images/photo01.jpg')  # get the img

thum = cv.CreateImage((im.width / 2, im.height / 2), 8, 3)
cv.Resize(im, thum)
cv.SaveImage('thum.jpg', thum)
