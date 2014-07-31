#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
import cv
import cv2
import numpy as np
import os

class _proc_img:

    def split_img(src_img,split_h,split_w):
        img = cv.LoadImage(src_img)
        fp = "/home/nooryes/VMshare/project/opencv/output/"
        suffix = ".jpg"
        fn = 0
        ceil_height = img.height/split_h
        ceil_width = img.width/split_w
        tmp_img = img
        sp_img_li = []
        for i in range(split_h):
            for j in range(split_w):
                tmp_img = img
                op_name = fp + repr(fn) + suffix
                cv.SetImageROI(tmp_img,(i + j*ceil_width,j + i*ceil_height,ceil_width,ceil_height))
                sp_img_li.append(tmp_img)
                cv.SaveImage(op_name,tmp_img)
                fn += 1
        return sp_img_li



src_img = sys.argv[1]
split_h = 5
split_w = 5
img = _proc_img()
img.split_img(src_img,split_h,split_w)
#sp_img_li =
