# @Description: Skeletonize.py
# @Author: 孤烟逐云zjy
# @Date: 2020/5/2 23:57
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/


# import cv2
# from skimage import morphology,draw, data, color
# import numpy as np
# import matplotlib.pyplot as plt

#创建一个二值图像用于测试
# image = np.zeros((400, 400))
#生成目标对象1(白色U型)
# image[10:-10, 10:100] = 1
# image[-100:-10, 10:-10] = 1
# image[10:-10, -100:-10] = 1
#
# #生成目标对象2（X型）
# rs, cs = draw.line(250, 150, 10, 280)
# for i in range(10):
#     image[rs + i, cs] = 1
# rs, cs = draw.line(10, 150, 250, 280)
# for i in range(20):
#     image[rs + i, cs] = 1
#
# #生成目标对象3（O型）
# ir, ic = np.indices(image.shape)
# circle1 = (ic - 135)**2 + (ir - 150)**2 < 30**2
# circle2 = (ic - 135)**2 + (ir - 150)**2 < 20**2
# image[circle1] = 1
# image[circle2] = 0
#
# #实施骨架算法
# skeleton =morphology.skeletonize(image)
#
# #显示结果
# fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
#
# ax1.imshow(image, cmap=plt.cm.gray)
# ax1.axis('off')
# ax1.set_title('original', fontsize=20)
#
# ax2.imshow(skeleton, cmap=plt.cm.gray)
# ax2.axis('off')
# ax2.set_title('skeleton', fontsize=20)
#
# fig.tight_layout()
# plt.show()



# 马骨架提取
# image = cv.imread("./images/photo01.jpg")
# image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
# image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
# image = 1 - image

# image=color.rgb2gray(data.horse())
# image=1-image #反相
#
# skeleton = morphology.skeletonize(image)
#
# # 显示结果
# fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
#
# ax1.imshow(image, cmap=plt.cm.gray)
# ax1.axis('off')
# ax1.set_title('original', fontsize=20)
#
# ax2.imshow(skeleton, cmap=plt.cm.gray)
# ax2.axis('off')
# ax2.set_title('skeleton', fontsize=20)
#
# fig.tight_layout()
# plt.show()


# 对人体建模
# 使用OpenCV库计算生态骨架（morphological  skeleton）

# im = cv2.imread('./images/photo01.jpg', cv2.IMREAD_GRAYSCALE)
# thresh, im = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# im = 255 - im
# cv2.imshow('binary.png', im)  # 控制背景为黑色
# cv2.imwrite("./images/photo01_w.jpg", im)
# dst = im.copy()
#
# num_erode = 1
#
# while (True):
#     if np.sum(dst) == 0:
#         break
#     kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
#     dst = cv2.erode(dst, kernel)
#     num_erode = num_erode + 1
#
# skeleton = np.zeros(dst.shape, np.uint8)
#
# for x in range(num_erode):
#     kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
#     dst = cv2.erode(im, kernel, None, None, x)
#     open_dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel)
#     result = dst - open_dst
#     skeleton = skeleton + result
#     cv2.waitKey(10)
#
# cv2.imshow('result', skeleton)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()





