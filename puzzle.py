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

        piece_pos_up = [id_index,0]
        piece_pos_down = [id_index,1]
        piece_pos_left = [id_index,2]
        piece_pos_right = [id_index,3]
        piece_content = cv2_img

        piece = Piece(id_index,piece_pos_up,piece_pos_down,piece_pos_left,piece_pos_right,piece_content)
        piece_list.append(piece)
        id_index += 1

    return piece_list

def calc_pixle_dis(src_piece_list,edge_depth = 10):

    #sqrt( (Xr-Yr)^2 + (Xg-Yg)^2 + (Xb-Yb)^2 )
    for src_piece in src_piece_list:

        src_cv2_img = src_piece.piece_content
        src_piece_h = src_cv2_img.shape[0]
        src_piece_w = src_cv2_img.shape[1]


        for w in range(src_piece_w):
            for h in range(edge_depth):

                #up
                #src_cv2_img[h,w] = [255,255,255]

                Xr_up = (src_cv2_img[h,w][0])
                Xg_up = (src_cv2_img[h,w][1])
                Xb_up = (src_cv2_img[h,w][2])

                #down
                #src_cv2_img[(src_piece_w-1)-h,w] = [255,255,255]

                Xr_down = (src_cv2_img[(src_piece_w-1)-h,w][0])
                Xg_down = (src_cv2_img[(src_piece_w-1)-h,w][1])
                Xb_down = (src_cv2_img[(src_piece_w-1)-h,w][2])

                #left
                #src_cv2_img[w,h] = [255,255,255]

                Xr_left = (src_cv2_img[w,h][0])
                Xg_left = (src_cv2_img[w,h][1])
                Xb_left = (src_cv2_img[w,h][2])

                #right
                #src_cv2_img[w,(src_piece_h-1)-h] = [255,255,255]

                Xr_right = (src_cv2_img[w,(src_piece_h-1)-h][0])
                Xg_right = (src_cv2_img[w,(src_piece_h-1)-h][1])
                Xb_right = (src_cv2_img[w,(src_piece_h-1)-h][2])

        #cv2.imshow("piece",src_cv2_img)
        #cv2.waitKey()
        #cv2.destroyAllWindows()

        #sqrt( (Xr-Yr)^2 + (Xg-Yg)^2 + (Xb-Yb)^2 )
        for des_piece in src_piece_list:
            if des_piece.piece_id == src_piece.piece_id:
                pass
            else:
                des_cv2_img = des_piece.piece_content
                des_piece_h = des_cv2_img.shape[0]
                des_piece_w = des_cv2_img.shape[1]

                if src_piece_w == des_piece_w and src_piece_h == des_piece_w:

                    print src_piece.piece_id
                    print des_piece.piece_id

                    for w in range(des_piece_w):
                        for h in range(edge_depth):

                            #up
                            #des_cv2_img[h,w] = [255,255,255]

                            Xr_up = (des_cv2_img[h,w][0])
                            Xg_up = (des_cv2_img[h,w][1])
                            Xb_up = (des_cv2_img[h,w][2])

                            #down
                            #des_cv2_img[(des_piece_w-1)-h,w] = [255,255,255]

                            Xr_down = (des_cv2_img[(des_piece_w-1)-h,w][0])
                            Xg_down = (des_cv2_img[(des_piece_w-1)-h,w][1])
                            Xb_down = (des_cv2_img[(des_piece_w-1)-h,w][2])

                            #left
                            #des_cv2_img[w,h] = [255,255,255]

                            Xr_left = (des_cv2_img[w,h][0])
                            Xg_left = (des_cv2_img[w,h][1])
                            Xb_left = (des_cv2_img[w,h][2])

                            #right
                            #des_cv2_img[w,(des_piece_h-1)-h] = [255,255,255]

                            Xr_right = (des_cv2_img[w,(des_piece_h-1)-h][0])
                            Xg_right = (des_cv2_img[w,(des_piece_h-1)-h][1])
                            Xb_right = (des_cv2_img[w,(des_piece_h-1)-h][2])


                #cv2.imshow("piece",des_cv2_img)
                #cv2.waitKey()
                #cv2.destroyAllWindows()

        print "#"*10

cv2_img_li = basic.read_img_cv2("split_output")
piece_list = piece_wrap(cv2_img_li)
calc_pixle_dis(piece_list)



