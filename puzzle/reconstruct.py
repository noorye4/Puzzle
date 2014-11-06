#!/usr/bin/env python
#-*- encoding: utf-8 -*-

# python libray
import sys
import os
import random
import math
from itertools import permutations
from time import time


# third party library
import cv
import cv2
import numpy as np


class Piece:

    def __init__(self, piece_id, edge_list, piece_pos):
        self.piece_id = piece_id
        self.edge_list = edge_list
        self.piece_pos = piece_pos


class Solution:

    def __init__(self, order_list, global_diff):
        self.order_list = order_list
        self.global_diff = global_diff


def wrap_piece_obj(src_piece_list, edge_depth=1):

    # init
    piece_obj_list = []
    piece_id = 0
    piece_pos = 0

    for src_piece in src_piece_list:

        src_piece_h = src_piece.shape[0]
        src_piece_w = src_piece.shape[1]

        edge_list = []

        edge_up = []
        edge_down = []
        edge_left = []
        edge_right = []

        for w in range(src_piece_w):
            for h in range(edge_depth):
                # up
                if h % 2 == 0:
                    src_piece[h,w] = [0,0,0]
                    src_piece[src_piece_h-edge_depth+h,w] = [0,0,0]
                else:
                    src_piece[h,w] = [255,255,255]
                    src_piece[src_piece_h-edge_depth+h,w] = [255,255,255]


                edge_up.append(src_piece[h, w])
                # down
                #src_piece[src_piece_h-edge_depth+h,w] = [0,0,0]
                edge_down.append(src_piece[src_piece_h - edge_depth + h, w])

        for h in range(src_piece_h):
            for w in range(edge_depth):
                # left
                if w % 2 == 0:
                    src_piece[h,w] = [0,0,0]
                    src_piece[h,src_piece_w-edge_depth+w] = [0,0,0]
                else:
                    src_piece[h,w] = [255,255,255]
                    src_piece[h,src_piece_w-edge_depth+w] = [255,255,255]

                #src_piece[h,w] = [0,0,0]
                edge_left.append(src_piece[h, w])
                # right
                #src_piece[h,src_piece_w-edge_depth+w] = [0,0,0]
                edge_right.append(src_piece[h, src_piece_w - edge_depth + w])

        #modify
        edge_list.append(edge_up)
        edge_list.append(edge_down)
        edge_list.append(edge_left)
        edge_list.append(edge_right)

        cv2.imshow('image', src_piece)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        piece = Piece(piece_id, edge_list, piece_pos)
        piece_obj_list.append(piece)
        piece_id += 1

    for i in piece_obj_list[0].edge_list[0]:
        print i
    for piece in piece_obj_list:
        print "#"*50
        for k in piece.edge_list:
            print "@"*50
            for j in k:
                print j
    return piece_obj_list


def parse_calc_edge(piece_obj_list):

    x = 1
    y = 0

    up = 0
    down = 1
    left = 2
    right = 3

    comb_list = []
    for src_piece in piece_obj_list:
        for des_piece in piece_obj_list:
            if src_piece.piece_id == des_piece.piece_id:
                pass
            else:
                src_x = src_piece.piece_pos[x]
                src_y = src_piece.piece_pos[y]

                des_x = des_piece.piece_pos[x]
                des_y = des_piece.piece_pos[y]

                if src_x + 1 == des_x and src_y == des_y:
                    comb_piece = [src_piece.piece_id, des_piece.piece_id]
                    comb_edge = [right, left]
                    comb0 = [comb_piece, comb_edge]
                    if comb0:
                        comb_list.append(comb0)
                if src_x - 1 == des_x and src_y == des_y:
                    comb_piece = [src_piece.piece_id, des_piece.piece_id]
                    comb_edge = [left, right]
                    comb1 = [comb_piece, comb_edge]
                    if comb1:
                        comb_list.append(comb1)
                if src_x == des_x and src_y + 1 == des_y:
                    comb_piece = [src_piece.piece_id, des_piece.piece_id]
                    comb_edge = [down, up]
                    comb2 = [comb_piece, comb_edge]
                    if comb2:
                        comb_list.append(comb2)
                if src_x == des_x and src_y - 1 == des_y:
                    comb_piece = [src_piece.piece_id, des_piece.piece_id]
                    comb_edge = [up, down]
                    comb3 = [comb_piece, comb_edge]
                    if comb3:
                        comb_list.append(comb3)

    return comb_list


def calc_order_diff(piece_obj_list, comb_list):
    total_edge_diff = 0
    for i in comb_list:
        src_piece_id = i[0][0]
        des_piece_id = i[0][1]
        src_edge_id = i[1][0]
        des_edge_id = i[1][1]

        # print src_piece_id,src_edge_id,des_piece_id,des_edge_id

        src_edge = piece_obj_list[src_piece_id].edge_list[src_edge_id]
        des_edge = piece_obj_list[des_piece_id].edge_list[des_edge_id]
        edge_diff = calc_edge_diff(src_edge, des_edge)
        total_edge_diff = total_edge_diff + edge_diff

    return total_edge_diff


def calc_edge_diff(src_edge, des_edge):

    #if len(src_edge) == len(des_edge):
    edge_len = len(src_edge)
    #if len(src_edge) > len(des_edge):
        #edge_len = len(des_edge)
    #if len(src_edge) < len(des_edge):
        #edge_len = len(src_edge)

    edge_diff = 0.0
    for pixel in range(edge_len):

        Xr = src_edge[pixel][0].astype(float)
        Xg = src_edge[pixel][1].astype(float)
        Xb = src_edge[pixel][2].astype(float)

        Yr = des_edge[pixel][0].astype(float)
        Yg = des_edge[pixel][1].astype(float)
        Yb = des_edge[pixel][2].astype(float)

        diff = np.sqrt((Xr - Yr) ** 2 + (Xg - Yg) ** 2 + (Xb - Yb) ** 2)
        #diff = math.sqrt((Xr - Yr) ** 2 + (Xg - Yg) ** 2 + (Xb - Yb) ** 2)
        edge_diff = edge_diff + diff

    return edge_diff


def remove_rep_comb(comb_list):
    for i in comb_list:
        for j in comb_list:

            a = [i[0][1], i[0][0]]
            b = [j[0][0], j[0][1]]
            if a == b:
                comb_list.remove(j)
    return comb_list


def set_piece_pos(piece_obj_list, order_list):

    index = 0
    for i in piece_obj_list:
        i.piece_pos = order_list[index]
        index += 1
    return piece_obj_list


def get_all_order_list(order_list):
    all_order_list = list(permutations(order_list))
    out = []
    for i in all_order_list:
        x = list(i)
        out.append(x)
    return out


def order_to_index(order_list, piece_obj_list):
    set_piece_pos(piece_obj_list, order_list)
    comb_order = sorted(piece_obj_list, key=lambda piece: piece.piece_pos)
    img_index = []
    for i in comb_order:
        img_index.append(i.piece_id)
    return img_index
