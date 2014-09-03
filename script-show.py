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
from puzzle2 import *
from basic import *

cv2_img_li = read_img_cv2("random_output")

piece_obj_list = wrap_piece_obj(cv2_img_li,20)

order_list = gen_order_list(2, 2)

set_piece_pos(piece_obj_list, order_list)

all_order_list = get_all_order_list(order_list)

solution_list = []

index = 0
for order_list in all_order_list:

    set_piece_pos(piece_obj_list, order_list)
    comb_list = get_calc_edge(piece_obj_list)
    comb_list = remove_rep_comb(comb_list)

    global_diff = calc_order_diff(piece_obj_list, comb_list)
    solution = Solution(order_list, global_diff)
    solution_list.append(solution)
    index += 1

solution_list = sorted(solution_list,key=lambda solution:solution.global_diff)

index = 0
f = open("solution.txt","w+")
for i in solution_list:
    s = repr(i.global_diff) 
    s1 = repr(i.order_list) 
    s2 = repr(index)

    f.write(s2 + "\n")
    f.write(s + "\n")
    f.write(s1 + "\n")
    index += 1
f.close()


for i in solution_list:
    img_index = order_to_index(i.order_list, piece_obj_list)
    print img_index
    output_comb_img(img_index)
    img_li = read_img_cv("comb_output")
    out_img =  combine_image(img_li)

    cv.ShowImage("img",out_img)
    cv.WaitKey(0)
    cv.DestroyAllWindows()