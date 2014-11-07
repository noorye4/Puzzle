#!/usr/bin/env python
#-*- encoding: utf-8 -*-

#python libray
import sys
import pickle

#puzzle library
sys.path.append("..")
from core.ImageOperating import *
from core.Reconstruct import *

input_sol = sys.argv[1]
solutions = load_solution(input_sol)
cv2_img_li = read_img_cv2("random_output")
piece_obj_list = wrap_piece_obj(cv2_img_li,1)
output_solu_img(solutions,piece_obj_list)
