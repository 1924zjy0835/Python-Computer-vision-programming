# @Description: imgByUrl.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/29 18:38
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import numpy as np
import urllib.request as urllib
import cv2 as cv

url = 'http://q87jey5py.bkt.clouddn.com/1586745385228.jpg'
resp = urllib.urlopen(url)
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv.imdecode(image, cv.IMREAD_COLOR)

cv.imshow("Image", image)
cv.waitKey(0)
cv.destroyAllWindows()