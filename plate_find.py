#encoding:utf-8
#pic2grey
import cv2
from squares import find_squares

from glob import glob

def pic2thres(pics_path):
	imglist = []	
	for fn in glob(pics_path):
		img_grey = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)
		img_thres = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
		imglist.append(img_thres)
	
	return imglist

def imgshow(imglist):
	for img in imglist:
		cv2.imshow('123', img)
		ch = 0xFF & cv2.waitKey()
		if ch == 27:
			break
	cv2.destroyAllWindows()

def squares(imglist):
	for img in imglist:
		squares = find_squares(img)
		cv2.drawContours( img, squares, -1, (5, 23, 140), 3 )
	imgshow(imglist)

def main():
	#设置图片路径
	pics_path = 'plates/*.jpg'

	#将图片灰度化，二值化
	imglist = pic2thres(pics_path)

	
	squares(imglist)

if __name__ == '__main__':
	main()