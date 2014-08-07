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

"""
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
"""

def calc_pixle_dis(piece_a,piece_b,edge_depth):

    index = 0
    piece_a_h = piece_a.shape[0]
    piece_a_w = piece_a.shape[1]
    print piece_a_h,piece_a_w

    #up side
    for w in range(piece_a_w):
        for h in range(edge_depth):
            print piece_a[255-h,w]
            #piece_a[h,w] = [0,0,0]
            #piece_a[255-h,w] = [0,0,0]
    #down side
    #for w in range(piece_a_w):
        #for h in range(edge_depth):
            #piece_a[255-h,w] = [0,0,0]

    cv2.imshow("piece_a",piece_a)
    cv2.waitKey()
    cv2.destroyAllWindows()

#sqrt( (Xr-Yr)^2 + (Xg-Yg)^2 + (Xb-Yb)^2 )
"""
    #left side
    for h in range(piece_a_h):
        for w in range(10):
            piece_a[h,w] = [0,0,0]
    #left side
    for h in range(piece_a_h):
        for w in range(10):
            piece_a[h,255-w] = [0,0,0]

"""

cv2_img_li = basic.read_img_cv2("split_output")
piece_a = cv2_img_li[0]
piece_b = cv2_img_li[1]
edge_depth = 10
calc_pixle_dis(piece_a,piece_b,edge_depth)
