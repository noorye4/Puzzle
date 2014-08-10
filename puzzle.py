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

class Piece:
    def __init__(self,piece_id,piece_pos_up,piece_pos_down,piece_pos_left,piece_pos_right,piece_content):
        self.piece_id = piece_id
        self.piece_pos_up = piece_pos_up
        self.piece_pos_down = piece_pos_down
        self.piece_pos_left = piece_pos_left
        self.piece_pos_right = piece_pos_right
        self.piece_content = piece_content

def piece_wrap(split_list):

    piece_list = []
    id_index = 0

    for cv2_img in split_list:

        piece_h = cv2_img.shape[0]
        piece_w = cv2_img.shape[1]

        piece_pos_up = 0
        piece_pos_down = 0
        piece_pos_left = 0
        piece_pos_right = 0
        piece_content = cv2_img

        piece = Piece(id_index,piece_pos_up,piece_pos_down,piece_pos_left,piece_pos_right,piece_content)
        piece_list.append(piece)
        id_index += 1

    return piece_list

def calc_pixle_dis(piece_list,edge_depth = 10):


    for piece in piece_list:
        print piece.piece_id

        cv2_img = piece.piece_content
        piece_h = cv2_img.shape[0]
        piece_w = cv2_img.shape[1]
        #up side
        for w in range(piece_w):
            for h in range(edge_depth):
                cv2_img[h,w] = [255,255,255]
                cv2_img[(piece_w-1)-h,w] = [255,255,255]
                cv2_img[w,h] = [255,255,255]
                cv2_img[w,(piece_h-1)-h] = [255,255,255]

        cv2.imshow("piece",cv2_img)
        cv2.waitKey()
        cv2.destroyAllWindows()
#sqrt( (Xr-Yr)^2 + (Xg-Yg)^2 + (Xb-Yb)^2 )
    #left side

cv2_img_li = basic.read_img_cv2("split_output")
piece_list = piece_wrap(cv2_img_li)
calc_pixle_dis(piece_list)



