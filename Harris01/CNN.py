# @Description: CNN.py
# @Author: 孤烟逐云zjy
# @Date: 2020/5/1 9:40
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def _convolve(image, kernel):
    h_kernel, w_kernel = kernel.shape
    h_image, w_image = image.shape

    res_h = h_image - h_kernel + 1
    res_w = w_image - w_kernel + 1

    res = np.zeros((res_h, res_w),np.uint8)
    for i in range(res_h):
        for j in range(res_w):
            res[i, j] = normal(image[i:i + h_kernel, j:j + w_kernel], kernel)

    return res


def normal(image, kernel):
    res = np.multiply(image, kernel).sum()

    if res > 255:
        return 255
    elif res < 0:
        return 0
    else:
        return res


def conv(image, kernel, mode='same'):
    if mode == 'fill':
        h = kernel.shape[0]
        w = kernel.shape[1]

        image = np.pad(image, ((h, h), (w, w), (0, 0)), 'constant')
    conv_b = _convolve(image[:, :, 0], kernel)
    conv_g = _convolve(image[:, :, 1], kernel)
    conv_r = _convolve(image[:, :, 2], kernel)
    res = np.dstack([conv_b, conv_g, conv_r])
    return res


if __name__ == '__main__':
    path = './images/girl01.jpg'
    image = cv.imread(path)

    # kernel 是一个3*3的边缘特征提取器，可以提取各个方向上的边缘
    # kernel2 是一个5*5的浮雕特征提取器

    kernel = np.array([
        [1, 1, 1],
        [1, -7.5, 1],
        [1, 1, 1]
    ])

    res = conv(image, kernel, 'fill')
    plt.imshow(res)
    plt.show()
