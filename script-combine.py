#!/usr/bin/env python
#-*- encoding: utf-8 -*-

#python libray
import sys
import os
import random

#third party library
import cv
import cv2
import numpy as np

#puzzle library
from basic import *

img_li = read_img_cv("comb_output")
out_img =  combine_image(img_li)

cv.ShowImage("img",out_img)
cv.WaitKey(0)
cv.DestroyAllWindows()

# output_cv_img(out_img)