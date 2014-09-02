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
import basic

try:
    src_img = sys.argv[1]
    split_h = int(sys.argv[2])
    split_w = int(sys.argv[3])
    #process split
    basic.split_img(src_img,split_h,split_w)

except:
    print " Usage : python main.py [src_image] [split_h] [split_w]"
    print "please input args !"