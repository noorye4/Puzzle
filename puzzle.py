#!/usr/bin/env python
#-*- encoding: utf-8 -*-

#python libray
import sys
import os
import random
import math

#third party library
import cv
import cv2
import numpy as np

#puzzle library
import basic

class Piece:
    def __init__(self,piece_id,edge_id,content,piece_pos,edge_diff):
        self.piece_id = piece_id
        self.edge_id = edge_id
        self.content = content
        self.piece_pos = piece_pos
        self.edge_diff = edge_diff

def get_edge_obj(src_piece_list,edge_depth=1):
    """
    up = 0
    down = 1
    left = 2
    right = 3
    """
    piece_id = 0
    edge_list = []
    piece_pos = [0,0]
    #sqrt( (Xr-Yr)^2 + (Xg-Yg)^2 + (Xb-Yb)^2 )
    for src_piece in src_piece_list:

        src_piece_h = src_piece.shape[0]
        src_piece_w = src_piece.shape[1]

        edge_up = []
        edge_down = []
        edge_left = []
        edge_right = []
        edge_diff = 0
        #edge math
        for w in range(src_piece_w):
            for h in range(edge_depth):

                #up
                #src_piece[h,w] = [245,245,245]

                Xr_up = (src_piece[h,w][0])
                Xg_up = (src_piece[h,w][1])
                Xb_up = (src_piece[h,w][2])

                pixel = [Xr_up,Xg_up,Xb_up]
                edge_up.append(pixel)
                up_edge_id = 0

                up_piece = Piece(piece_id,up_edge_id,edge_up,piece_pos,edge_diff)

                #down
                #src_piece[(src_piece_w-1)-h,w] = [255,255,255]
                Xr_down = (src_piece[(src_piece_w-1)-h,w][0])
                Xg_down = (src_piece[(src_piece_w-1)-h,w][1])
                Xb_down = (src_piece[(src_piece_w-1)-h,w][2])
                pixel = [Xr_down,Xg_down,Xb_down]
                edge_down.append(pixel)
                down_edge_id = 1
                down_piece = Piece(piece_id,down_edge_id,edge_down,piece_pos,edge_diff)

                #left
                #src_piece[w,h] = [255,255,255]
                Xr_left = (src_piece[w,h][0])
                Xg_left = (src_piece[w,h][1])
                Xb_left = (src_piece[w,h][2])
                pixel = [Xr_left,Xg_left,Xb_left]
                edge_left.append(pixel)
                left_edge_id = 2
                left_piece= Piece(piece_id,left_edge_id,edge_left,piece_pos,edge_diff)

                #right
                #src_piece[w,(src_piece_h-1)-h] = [255,255,255]
                Xr_right = (src_piece[w,(src_piece_h-1)-h][0])
                Xg_right = (src_piece[w,(src_piece_h-1)-h][1])
                Xb_right = (src_piece[w,(src_piece_h-1)-h][2])
                pixel = [Xr_right,Xg_right,Xb_right]
                edge_right.append(pixel)
                right_edge_id = 3
                right_piece= Piece(piece_id,right_edge_id,edge_right,piece_pos,edge_diff)

        edge_list.append(up_piece)
        edge_list.append(down_piece)
        edge_list.append(left_piece)
        edge_list.append(right_piece)

        piece_id += 1
    return edge_list


def get_edge_diff(i_piece,j_piece):

    if len(i_piece.content) == len(j_piece.content):
        edge_len = len(i_piece.content)
    if len(i_piece.content) >  len(j_piece.content):
        edge_len = len(j_piece.content)
    if len(i_piece.content) <  len(j_piece.content):
        edge_len = len(i_piece.content)

    total_diff = 0
    for k in range(edge_len):

        Xr = i_piece.content[k][0]
        Xg = i_piece.content[k][1]
        Xb = i_piece.content[k][2]

        Yr = j_piece.content[k][0]
        Yg = j_piece.content[k][1]
        Yb = j_piece.content[k][2]

        diff = math.sqrt((Xr-Yr)^2 + (Xg-Yg)^2 + (Xb-Yb)^2)
        total_diff = total_diff + diff
    return total_diff



def calc_piece_pos(edge_obj_list):
    index = 0
    tag = " | "
    for i in edge_obj_list:
        count = 0
        for j in edge_obj_list:

            if i.piece_id == j.piece_id:
                pass
            else:

                print i.piece_id , i.edge_id ,tag, j.piece_id , j.edge_id

                i.edge_diff = get_edge_diff(i,j)
                #cur_diff = i.edge_diff

                #print i.edge_diff
                #if count == 0:
                   #cur_diff = edge_diff
                #if edge_diff < cur_diff :
                    #cur_diff = edge_diff

                print "-"*10
                count += 1
                index += 1
        print cur_diff

        print "#"*20
    print index

cv2_img_li = basic.read_img_cv2("split_output")

edge_obj_li = get_edge_obj(cv2_img_li)

calc_piece_pos(edge_obj_li)

