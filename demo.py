# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract

plate = Image.open('plate.jpg')
print(pytesseract.image_to_string(plate, lang='chi_sim'))