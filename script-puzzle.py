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

# print os.listdir("random_output")

# cv2.imshow('image',cv2_img_li[1])
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print len(cv2_img_li)
# for i in cv2_img_li:
#     cv2.imshow('image',i)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


piece_obj_list = wrap_piece_obj(cv2_img_li)
order_list = basic.gen_order_list(2, 2)
# set_piece_pos(piece_obj_list, order_list)

all_order_list = get_all_order_list(order_list)

solution_list = []

index = 0
for order_list in all_order_list:

    # print index
    set_piece_pos(piece_obj_list, order_list)
    comb_list = get_calc_edge(piece_obj_list, order_list)
    comb_list = remove_rep_comb(comb_list)

    global_diff = calc_order_diff(piece_obj_list, comb_list)
    solution = Solution(order_list, global_diff)
    solution_list.append(solution)
    index += 1

solution_list = sorted(solution_list,key=lambda solution:solution.global_diff)

print solution_list[0].order_list

# solu_to_index(solution_list[0],piece_obj_list)

print "#"*20
index = 0
for solution in solution_list:
    print index,solution.order_list
    print solution.global_diff
    index += 1