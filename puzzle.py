#!/usr/bin/env python
#-*- encoding: utf-8 -*-

#python libray
import sys
import os

#third party library
import cv
import cv2
import numpy as np

#my library
from mutli_dis import combineImages

def split_img(src_img,split_h,split_w):
    #check file is exists
    if os.path.exists("output"):
        os.system('rm -r output')
        print "delete output"
    os.system('mkdir output')

    img = cv.LoadImage(src_img)
    fp = os.getcwd() + "/" +  "output" + "/"
    print fp
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

def read_img_cv2(img_dir):
    cv2_img_li = []
    for i in os.listdir(img_dir):
        cv2_img = cv2.imread(img_dir + "/" + i)
        cv2_img_li.append(cv2_img)

def read_img_cv(img_dir):
    cv_img_li = []
    for i in os.listdir(img_dir):
        cv_img = cv.LoadImage(img_dir + "/" + i)
        cv_img_li.append(cv_img)
    return cv_img_li
#args
src_img = sys.argv[1]
split_h = int(sys.argv[2])
split_w = int(sys.argv[3])

#func run
split_img(src_img,split_h,split_w)
img_li = read_img_cv("output")
for i in img_li:
    print i.
cv.SaveImage("out.jpg", combineImages(img_li))










