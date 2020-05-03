# @Description: SIFT.py
# @Author: 孤烟逐云zjy
# @Date: 2020/5/2 13:02
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2 as cv
import urllib.request as urllib
import numpy as np


url = 'http://127.0.0.1:8088/media/photo01.min.jpg'


def sift(img_url):
    resp = urllib.urlopen(img_url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    img = cv.imdecode(image, cv.IMREAD_COLOR)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # opencv将SIFT()算法整合到xfeatures2d集合里面了
    # sift = cv.SFIT()
    sift = cv.xfeatures2d.SIFT_create()

    kp = sift.detect(gray, None)
    # cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    img = cv.drawKeypoints(gray, kp, img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG)
    cv.imshow("sift_image", img)
    # return img

# img = cv.imread(url)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
# # opencv将SIFT()算法整合到xfeatures2d集合里面了
# # sift = cv.SFIT()
# sift = cv.xfeatures2d.SIFT_create()
#
# kp = sift.detect(gray, None)
# # cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
# img = cv.drawKeypoints(gray, kp, img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG)
# cv.imshow("sift_images", img)


sift(url)
cv.waitKey(0)
cv.destroyAllWindows()

