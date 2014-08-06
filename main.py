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

def main():
    #args
    print " Usage : python main.py [src_image] [split_h] [split_w]"
    try:
        src_img = sys.argv[1]
        split_h = int(sys.argv[2])
        split_w = int(sys.argv[3])
        #process split
        basic.split_img(src_img,split_h,split_w)
        #process read
        split_img_li = basic.read_img_cv("split_output")

        random.shuffle(split_img_li)
        out_img =  basic.combine_image(split_img_li)
        basic.output_cv_img(out_img)
    except:
        print "please input args !"

if __name__ == '__main__':
    main()

