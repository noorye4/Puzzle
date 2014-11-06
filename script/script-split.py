#!/usr/bin/env python
#-*- encoding: utf-8 -*-

#python libray
import sys

#puzzle library
sys.path.append("..")
from itertools import *
from puzzle.basic import *
from puzzle.reconstruct import *

try:
    src_img = sys.argv[1]
    split_h = int(sys.argv[2])
    split_w = int(sys.argv[3])
    #process split
    split_img(src_img,split_h,split_w)

except:
    print " Usage : python script-split.py [src_image] [split_h] [split_w]"
    print "please input args !"
