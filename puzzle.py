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

def calc_pixle_dis():

    cv_img_li = basic.read_img_cv("split_output")
    img = cv_img_li[0]
    print img.width , img.height
    index = 0
    for w in range(img.width):
        s = cv.Get2D(img,w,0)
        s.val[0] = 255
        print index ,s
        index += 1
    #x =  cv2_img_li[0]
    #print x
    cv.ShowImage("image",img)
    cv.WaitKey()
    cv.DestroyAllWindows()

def calc_pixle_dis_1():

    cv2_img_li = basic.read_img_cv2("split_output")
    img = cv2_img_li[0]
    index = 0
    img_h = img.shape[0]
    img_w = img.shape[1]
    print img_h,img_w

    #up side
    for w in range(img_w):
        for h in range(10):
            img[h,w] = [0,0,0]
    #left side
    for h in range(img_h):
        for w in range(10):
            img[h,w] = [0,0,0]
    #down side
    for w in range(img_w):
        for h in range(10):
            img[255-h,w] = [0,0,0]
    #left side
    for h in range(img_h):
        for w in range(10):
            img[h,255-w] = [0,0,0]


    cv2.imshow("img",img)
    cv2.waitKey()
    cv2.destroyAllWindows()



calc_pixle_dis_1()
