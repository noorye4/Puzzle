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
    def __init__(self,piece_id,piece_pos_up,piece_pos_down,piece_pos_left,piece_pos_right):
        self.piece_id = piece_id
        self.piece_pos_up = piece_pos_up
        self.piece_pos_down = piece_pos_down
        self.piece_pos_left = piece_pos_left
        self.piece_pos_right = piece_pos_right

def piece_tag(split_list,edge_depth):

    id_index = 0
    for cv2_img in split_list:

        piece_h = cv2_img.shape[0]
        piece_w = cv2_img.shape[1]


        #up side
        for w in range(piece_w):
            for h in range(edge_depth):
                cv2_img[h,w] = [255,255,255]
                cv2_img[(piece_w-1)-h,w] = [255,255,255]
        ##down side
        #for w in range(piece_w):
            #for h in range(edge_depth):
                #cv2_img[(piece_w-1)-h,w] = [255,255,255]

        ##right side
        for h in range(piece_h):
            for w in range(edge_depth):
                cv2_img[h,w] = [255,255,255]
                cv2_img[h,(piece_w-1)-w] = [255,255,255]

        ##left side
        #for h in range(piece_h):
            #for w in range(edge_depth):
                #cv2_img[h,255-w] = [255,255,255]

        id_index += 1
        print id_index ,piece_h,piece_w
        cv2.imshow("img",cv2_img)
        cv2.waitKey()
        cv2.destroyAllWindows()





#def calc_pixle_dis(piece_a,piece_b,edge_depth):

    #index = 0
    #piece_a_h = piece_a.shape[0]
    #piece_a_w = piece_a.shape[1]
    #print piece_a_h,piece_a_w

    ##up side
    #for w in range(piece_a_w):
        #for h in range(edge_depth):
            ##print piece_a[255-h,w]
            #piece_a[h,w] = [255,2550,255]
    ##down side
    #for w in range(piece_a_w):
        #for h in range(edge_depth):
            #piece_a[255-h,w] = [255,255,255]

    ##right side
    #for h in range(piece_a_h):
        #for w in range(10):
            #piece_a[h,w] = [255,255,255]
    #left side
    #for h in range(piece_a_h):
        #for w in range(10):
            #piece_a[h,255-w] = [255,255,255]

    #cv2.imshow("piece_a",piece_a)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

#sqrt( (Xr-Yr)^2 + (Xg-Yg)^2 + (Xb-Yb)^2 )
    #left side

cv2_img_li = basic.read_img_cv2("split_output")
#piece_a = cv2_img_li[0]
#piece_b = cv2_img_li[1]
edge_depth = 10
#calc_pixle_dis(piece_a,piece_b,edge_depth)
piece_tag(cv2_img_li,edge_depth)



