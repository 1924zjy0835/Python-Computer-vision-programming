# @Description: setMouseCallback.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/27 8:49
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

# 安装opencv-python
import cv2 as cv


events = [i for i in dir(cv) if 'EVENT' in i]
print(events)