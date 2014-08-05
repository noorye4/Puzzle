#!/usr/bin/env python
#-*- encoding: utf-8 -*-

#python libray
import sys
import os
import random
import math
from operator import attrgetter

#third party library
import cv
import cv2
import numpy as np


def split_img(src_img,split_h,split_w):
    #check file is exists
    if os.path.exists("split_output"):
        os.system('rm -r split_output')
        print "delete split_output"
    os.system('mkdir split_output')

    img = cv.LoadImage(src_img)
    fp = os.getcwd() + "/" +  "split_output" + "/"
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

def combine_image(imageArray):

    numImages = len(imageArray)
    colWidth = max(imageArray, key=attrgetter('width')).width
    rowHeight = max(imageArray, key=attrgetter('height')).height
    grid = int(math.ceil(math.sqrt(numImages)))
    combinedImage = cv.CreateImage((colWidth * grid, rowHeight * grid), 8, 3)
    cv.Set(combinedImage, cv.CV_RGB(50, 50, 50))

    for index, img in enumerate(imageArray):
        if img.nChannels == 1:
            colourImg = cv.CreateImage((img.width, img.height), 8, 3)
            cv.CvtColor(img, colourImg, cv.CV_GRAY2RGB)
            img = colourImg

        row = index % grid
        column = int(math.ceil(index / grid))
        cv.SetImageROI(
            combinedImage, (row * colWidth, column * rowHeight, img.width, img.height))
        cv.Copy(img, combinedImage)
        cv.ResetImageROI(combinedImage)

    return combinedImage

def read_img_cv2(img_dir):
    cv2_img_li = []
    for i in os.listdir(img_dir):
        cv2_img = cv2.imread(img_dir + "/" + i)
        cv2_img_li.append(cv2_img)
    return cv2_img_li

def read_img_cv(img_dir):
    cv_img_li = []
    img_li = (os.listdir(img_dir))
    img_li.sort(key=lambda x:int(x[:-4]))
    for i in img_li:
        cv_img = cv.LoadImage(img_dir + "/" + i)
        cv_img_li.append(cv_img)
    return cv_img_li

def output_cv_img(src_img):

    if os.path.exists("final_output"):
        os.system('rm -r final_output')
        print "delete final_output"
    os.system('mkdir final_output')

    output_dir = "final_output/out.jpg"
    cv.SaveImage(output_dir,src_img)




















