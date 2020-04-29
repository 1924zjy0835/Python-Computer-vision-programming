# @Description: GrabCut.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/28 23:16
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


src = cv.imread('./images/messi5.jpg')

# 创建一个src一样长宽的黑色图片
mask = np.zeros(src.shape[:2], np.uint8)

newmask = cv.imread('./images/messi502.jpg',0)
#
# cv.imshow('newmask', newmask)

# 根据新的掩模图像对原来的掩模图像进行编辑
mask[newmask == 0] = 0
mask[newmask == 255] = 1

bdgModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
#
# # grabCut(输入图像img, 掩模图像mask, 包含前景的矩形rect，(算法内部使用的数组)bdgModel/fgdModel、iterCount(算法的迭代次数))
mask, bgdModel, fgdModel = cv.grabCut(src, mask, None, bdgModel, fgdModel, 8, cv.GC_INIT_WITH_MASK)

# rect = (50, 50, 450, 290)  # (x, y, w, h)

# cv.grabCut(src, mask, rect, bdgModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)

mask = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')

src = src*mask[:, :, np.newaxis]

plt.imshow(src)
plt.colorbar()
plt.show()


# cv.waitKey(0)
# cv.destroyAllWindows()
