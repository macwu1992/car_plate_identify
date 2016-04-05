#encoding:utf-8
#pic2grey
import cv2
import numpy as np
#将图像读取出来
from glob import glob
for fn in glob('plates/*.jpg'):
	#转换为灰度图像
	img_grey = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)
	img0 = cv2.resize(img_grey, (800,600))
	#利用竖向纹理筛选车牌
	img1 = cv2.Sobel(img0, cv2.CV_8U, 0, 3, ksize = 9)
	# img1 = cv2.Canny(img_grey, 50, 150, 3)
	img = cv2.normalize(img1, cv2.NORM_MINMAX)
	#python中二值化 threshold 返回两个参数，使用（_, img_thres）来接受两个返回值
	_, img_thres = cv2.threshold(img1, 100, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

	#膨胀操作，对细小的部分进行融合
	dilate(img_thres, Mat(5,5,CV_8U),Point(-1,-1),2)
	cv2.imshow('123', img_thres)
	ch = 0xFF & cv2.waitKey()
	if ch == 27:
		break
	cv2.destroyAllWindows()