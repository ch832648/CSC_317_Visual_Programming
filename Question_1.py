# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:02:24 2019

@author: Caity
"""

import cv2
import numpy as np

#read a image using imread 
img = cv2.imread('../0-data/messi5.jpg', 0)
#rows,cols = img.shape
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst = cv2.warpAffine(dst, M, (cols,rows))

cv2.imshow('image',dst)

cv2.waitKey(0)

