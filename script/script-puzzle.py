#!/usr/bin/env python
#-*- encoding: utf-8 -*-

#python libray
import sys
import pickle

#puzzle library
sys.path.append("..")
from puzzle.basic import *
from puzzle.reconstruct import *

input_folder = sys.argv[1]
split_h = int(sys.argv[2])
split_w = int(sys.argv[3])

cv2_img_li = read_img_cv2(input_folder)

piece_obj_list = wrap_piece_obj(cv2_img_li,1)

order_list = gen_order_list(split_w, split_h)

set_piece_pos(piece_obj_list, order_list)

all_order_list = get_all_order_list(order_list)

solution_list = []

index = 0
for order_list in all_order_list:

    set_piece_pos(piece_obj_list, order_list)
    comb_list = parse_calc_edge(piece_obj_list)
    comb_list = remove_rep_comb(comb_list)

    global_diff = calc_order_diff(piece_obj_list, comb_list)
    solution = Solution(order_list, global_diff,piece_obj_list)
    solution_list.append(solution)
    index += 1

solution_list = sorted(solution_list,key=lambda solution:solution.global_diff)

index = 0
f = open("solutions.txt","w+")
for i in solution_list:
    s = repr(i.global_diff) 
    s1 = repr(i.order_list) 
    s2 = repr(index)

    f.write(s2 + "\r\n")
    f.write(s + "\r\n")
    f.write(s1 + "\r\n")
    index += 1
f.close()

f = open("solutions.sol","wb")
try:
    for i in solution_list:
        pickle.dump(i, f)
    f.close()
except:
    f.close()

# f = open("solutions.sol","rb")
# solutions = []
# while 1:
#     i = pickle.load(f)
#     print i.global_diff
#     solutions.append(i)

# print "Usage python script-puzzle.py [src dir] [split_h] [split_w]"
# print "pleasr input args !"
