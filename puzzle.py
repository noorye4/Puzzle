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

    cv2_img_li = basic.read_img_cv2("split_output")
    for i in cv2_img_li:
       print i.shape


    #x =  cv2_img_li[0]
    #print x
    #cv2.imshow('image',x)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()



calc_pixle_dis()
