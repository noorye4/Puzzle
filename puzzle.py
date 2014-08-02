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
import mutli_dis

def split_img(src_img,split_h,split_w):
    img = cv.LoadImage(src_img)
    os.system('rm -r output')
    print "delete output"
    os.system('mkdir output')
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

def read_img_cv2(pic_dir):
    cv2_img_li = []
    for i in os.listdir(pic_dir):
        cv2_img = cv2.imread(pic_dir + "/" + i)
        cv2_img_li.append(cv2_img)

src_img = sys.argv[1]
split_h = int(sys.argv[2])
split_w = int(sys.argv[3])

sp_img_li = split_img(src_img,split_h,split_w)
print sp_img_li

x1 = "output/0.jpg"
x2 = "output/1.jpg"
img1 = cv.LoadImage(x1)
img2 = cv.LoadImage(x2)
final_output = mutli_dis.combineImages(img1,img2)
print final_output
#cv.SaveImage("final_output",finl_output)















