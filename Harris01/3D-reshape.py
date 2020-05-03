# @Description: 3D-reshape.py
# @Author: 孤烟逐云zjy
# @Date: 2020/5/2 21:58
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/


import numpy as np
import homography
import sfm
import sift

# 标定矩阵
K = np.array([[2394,0,932],[0,2398,628],[0,0,1]])
# 载入图像，并计算特征
im1 = np.array(Image.open('alcatraz1.jpg'))
sift.process_image('alcatraz1.jpg','im1.sift')
l1,d1 = sift.read_features_from_file('im1.sift')
im2 = array(Image.open('alcatraz2.jpg'))
sift.process_image('alcatraz2.jpg','im2.sift')
l2,d2 = sift.read_features_from_file('im2.sift')
# 匹配特征
matches = sift.match_twosided(d1,d2)
ndx = matches.nonzero()[0]
# 使用齐次坐标表示，并使用 inv(K) 归一化
x1 = homography.make_homog(l1[ndx,:2].T)
ndx2 = [int(matches[i]) for i in ndx]
x2 = homography.make_homog(l2[ndx2,:2].T)
x1n = dot(inv(K),x1)
x2n = dot(inv(K),x2)
# 使用 RANSAC 方法估计 E
model = sfm.RansacModel()
E,inliers = sfm.F_from_ransac(x1n,x2n,model)
# 计算照相机矩阵（P2 是 4 个解的列表）
P1 = array([[1,0,0,0],[0,1,0,0],[0,0,1,0]])
P2 = sfm.compute_P_from_essential(E)
