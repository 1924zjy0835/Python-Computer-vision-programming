# @Description: KeyPointDetection.py
# @Author: 孤烟逐云zjy
# @Date: 2020/5/3 1:33
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/


from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import cv2

annFile = './json/person_keypoints_val2020.json'

# initialize COCO api for instance annotations
coco = COCO(annFile)  # 初始化coco对象

temp = coco.getCatIds()  # 获取“categories”中所有子节点的id，返回id列表

# display COCO categories and supercategories
cats = coco.loadCats(temp)  # 获取“categories”中的节点

nms = [cat['name'] for cat in cats]  # categories节点的子节点中的“name” 属性
print('COCO categories: \n{}\n'.format(' '.join(nms)))

nms = set([cat['supercategory'] for cat in cats])  # categories子节点的“supercategory” 属性
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories, select one at random
catIds = coco.getCatIds(catNms=['person', 'dog', 'skateboard'])  # 由 类别名称 获取类别id
imgIds = coco.getImgIds(catIds=catIds)  # 根据类别id 获取这一类的图像id(图像编号)
imgIds = coco.getImgIds(imgIds=imgIds)  # 根据图像编号（id） 获取图像的id(编号)

for i in range(len(imgIds)):
    img = coco.loadImgs(imgIds[i])[0]  # 根据图像编号（id） 在image节点下寻找子节点

    # load and display image
    # I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))
    # use url to load image
    print("D:\\Git02\\Git02\\Python-Computer-vision-programming\\Python-Computer-vision-programming\\Harris01\\cocodata\\" + img['file_name'])  # 获取image子节点的“file_name”属性

    I = io.imread("D:\\Git02\\Git02\\Python-Computer-vision-programming\\Python-Computer-vision-programming\\Harris01\\cocodata\\" + img['file_name'])

    # load and display instance annotations
    plt.imshow(I)
    plt.axis('off')

    annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds,
                            iscrowd=None)  # 根据image子节点中的id 、类别id 寻找对应的 “annotations”中的id
    anns = coco.loadAnns(annIds)  # 根据“annotations”子节点中的id 寻找对应此id对应的zi节点
    coco.showAnns(anns)  # 将“annotations”子节点中的segmentation属性和keypoints属性加载到图像上；

    plt.savefig('./result/temp%d.png' % i)  # 存储图片，可选
    plt.close("all")
    image_temp = cv2.imread("./result/temp%d.png" % i)
    cv2.imshow("test", image_temp)
    cv2.waitKey(10)
# 由于plt Agg 问题在vscode中显示不出来，用python-opencv 过度了一下。凑活看吧！
