# # @Description: Harris01.py
# # @Author: 孤烟逐云zjy
# # @Date: 2020/4/26 11:30
# # @SoftWare: PyCharm
# # @CSDN: https://blog.csdn.net/zjy123078_zjy
# # @博客园: https://www.cnblogs.com/guyan-2020/
#
# # PIL只是对于python2.x版本而言，对于python3.x版本来说可以通过下载pillow ：pip install pillow
# from PIL import Image
# # pylab 库是存在matplotlib中的，所以可以通过安装matplotlib下载：pip install matplotlib
# from pylab import *
# from matplotlib.font_manager import FontProperties
#
#
# font = FontProperties(fname=r"C:\windows\fonts\SimSun.tcc", size=14)
# figure()
#
# pil_im = Image.open('F:\Python计算机视觉编程\PCV-book-data\data\empire.jpg')
# gray()
# subplot(121)
# title(u'原图', font)
# axes('off')
# imshow(pil_im)
#
# pil_im = Image.open("F:\Python计算机视觉编程\PCV-book-data\data\empire.jpg").convert('L')
# subplot(122)
# title(u'灰度图', font)
# axes('off')
# imshow(pil_im)
#
# show()
