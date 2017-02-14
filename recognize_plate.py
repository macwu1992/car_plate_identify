# -*- coding: utf-8 -*-

# 这个模块的用途是识别车牌中的文字
__author__  = 'WuTong'

import cv2

def recognize(plate_img):
    # 车牌的灰度化
    # plate_img = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    # 车牌的二值化
    _, img_thres = cv2.threshold(plate_img, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite('plate.jpg', img_thres)
    return img_thres