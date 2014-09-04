#!/usr/bin/env python
#-*- encoding: utf-8 -*-

#python libray
import sys
import pickle

#puzzle library
sys.path.append("..")
from puzzle.basic import *
from puzzle.reconstruct import *

input_sol = sys.argv[1]
for i in load_solution(input_sol):
    print i.global_diff
    print i.order_list
    img_index = order_to_index(i.order_list, i.piece_obj_list)
    print img_index



