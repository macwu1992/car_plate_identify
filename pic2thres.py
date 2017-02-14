#encoding:utf-8
#pic2grey
import cv2
import numpy as np

#OpenCV定义的结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(20, 2))
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(1, 3))

imglist = []
originlist = []

def squares(imglist, originlist):
	i = 0
	for img in imglist:
		im2, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		for tours in contours:
			rc = cv2.boundingRect(tours)
            #rc[0] 表示图像左上角的纵坐标，rc[1] 表示图像左上角的横坐标，rc[2] 表示图像的宽度，rc[3] 表示图像的高度，
			if (rc[2]/rc[3]>1.8) & (rc[2]/rc[3]<6) & (rc[2]*rc[3]>3000):
                # originlist[i][rc[0]:rc[0]+rc[2],rc[1]:rc[1]+rc[3]]
				print rc
				cv2.rectangle(originlist[i], (rc[0],rc[1]),(rc[0]+rc[2],rc[1]+rc[3]),(255,0,123), 2)
                plate = originlist[i][rc[0]:rc[0]+rc[2], rc[1]:rc[1]+rc[3]]
		i += 1
	return originlist



def imgshow(imglist):
	for img in imglist:
		cv2.imshow('123', img)
		ch = 0xFF & cv2.waitKey()
		if ch == 27:
			break
	cv2.destroyAllWindows()



from glob import glob
#将图像读取出来
for fn in glob('plates/*.jpg'):
	originlist.append(cv2.imread(fn))

	#转为灰度图
	img = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)

	#利用竖向纹理筛选车牌，第三四个参数，决定竖向纹理的筛选
	img = cv2.Sobel(img, cv2.CV_8U, 2, 0, ksize = 3)

	#python中二值化 threshold 返回两个参数，使用（_, img_thres）来接受两个返回值
	_, img_thres = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

	#中值去噪
	img = cv2.medianBlur(img_thres, 3)

#膨胀操作：对细小的部分抹去，求kernel与图像区域的像素点的最大值，故白色区域增加
	img = cv2.dilate(img_thres, kernel, 30)

#腐蚀操作：对细小的部分加强，求kernel与图像区域的像素点的最大值，故白色区域减少
	img = cv2.erode(img, kernel1, 5)

	#闭运算：先膨胀后腐蚀的过程，用于连接被误分为小块的元素
	# img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, 3)

	#开运算：其实就是先腐蚀后膨胀的过程
	# opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel1, iterations = 1)
	imglist.append(img)

imgshow(squares(imglist, originlist))