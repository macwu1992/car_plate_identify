# -*- coding: utf-8 -*-
# 主程序
import cv2
import localize_plate, recognize_plate

def imgshow(imglist):
  for img in imglist:
    cv2.imshow('123', img)
    ch = 0xFF & cv2.waitKey()
    if ch == 27:
	  break
    cv2.destroyAllWindows()

if __name__ == '__main__':
  path = 'plates\*.jpg'
  plate_img = localize_plate.localize(path)
  recoged_plate = recognize_plate.recognize(plate_img)

  cv2.imshow('main', recoged_plate)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

