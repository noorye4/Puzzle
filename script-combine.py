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

split_img_li = basic.read_img_cv("split_output")
# random.shuffle(split_img_li)
out_img =  basic.combine_image(split_img_li)
basic.output_cv_img(out_img)