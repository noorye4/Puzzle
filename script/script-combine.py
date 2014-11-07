#!/usr/bin/env python
#-*- encoding: utf-8 -*-

#python libray
import sys

#puzzle library
sys.path.append("..")
from itertools import *
from core.ImageOperating import *
from core.Reconstruct import *

try:
    folder = sys.argv[1]
    img_li = read_img_cv(folder)
    out_img =  combine_image(img_li)
    output_cv_img(out_img)
except:
    print " Usage : python script-combine.py [img dir]"
    print "please input args !"
