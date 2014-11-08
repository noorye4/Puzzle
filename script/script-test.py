#!/usr/bin/env python
#-*- encoding: utf-8 -*-

# python libray
import sys
import pickle
from time import time

# puzzle library
sys.path.append("..")
from core.ImageOperating import *
from core.Reconstruct import *

if (len(sys.argv)) < 2:
    print "Usage python script-puzzle [input folder] [split_h] [split_w] [output]"

input_folder = sys.argv[1]
split_h = int(sys.argv[2])
split_w = int(sys.argv[3])
edge_depth = int(sys.argv[4])
output = str(sys.argv[5])

output_txt = output + ".txt"
output_sol = output + ".sol"

cv2_img_li = read_img_cv2(input_folder)
piece_obj_list = wrap_piece_obj(cv2_img_li,edge_depth)

"""
order_list = gen_order_list(split_w, split_h)
set_piece_pos(piece_obj_list, order_list)
all_order_list = get_all_order_list(order_list)
solution_list = []

combs = len(all_order_list)

for i in progressbar(range(combs), "Computing: ", 40):
    set_piece_pos(piece_obj_list, all_order_list[i])
    comb_list = parse_calc_edge(piece_obj_list)
    comb_list = remove_rep_comb(comb_list)

    global_diff = calc_order_diff(piece_obj_list, comb_list,edge_depth, )
    solution = Solution(all_order_list[i], global_diff)
    solution_list.append(solution)

solution_list = sorted(
    solution_list, key=lambda solution: solution.global_diff)

index = 0
f_txt = open(output_txt, "w+")
f_sol = open(output_sol, "wb")

try:
    for i in solution_list:
        str_global_diff = repr(i.global_diff)
        str_order_list = repr(i.order_list)
        #print i.order_list
        str_index = repr(index)

        f_txt.write(str_index + "\r\n")
        f_txt.write(str_global_diff + "\r\n")
        f_txt.write(str_order_list + "\r\n")
        pickle.dump(i, f_sol)

        index += 1

    f_sol.close()
    f_txt.close()
except:
    f_sol.close()
"""
