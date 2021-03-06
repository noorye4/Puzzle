#/usr/bin/env python
#-*- encoding: utf-8 -*-

# python libray
import sys
import os
import random
import math
import pickle
from string import split
from operator import attrgetter
from itertools import permutations

# third party library
import cv
import cv2
import numpy as np
from Reconstruct import *


class ImgIndex:

    def __init__(self, img_index, img):
        self.img_index = img_index
        self.img = img


def split_img(src_img, split_h, split_w):
    # check file is exists
    if os.path.exists("split_output"):
        os.system('rm -r split_output')
        print "delete split_output"
    os.system('mkdir split_output')

    img = cv.LoadImage(src_img)
    fp = os.getcwd() + "/" + "split_output" + "/"
    suffix = ".jpg"
    fn = 0
    ceil_height = img.height / split_h
    ceil_width = img.width / split_w
    #print ceil_width,ceil_height
    #print "#"*10
    tmp_img = img
    sp_img_li = []
    for i in range(split_h):
        for j in range(split_w):
            tmp_img = img
            op_name = fp + repr(fn) + suffix
            x =  i* ceil_width
            y =  j* ceil_height
            #print x,y
            cv.SetImageROI(
                tmp_img,
                (j * ceil_width, i * ceil_height, ceil_width, ceil_height))
            sp_img_li.append(tmp_img)
            cv.SaveImage(op_name, tmp_img)
            fn += 1


def combine_image(image_array):

    numImages = len(image_array)
    colWidth = max(image_array, key=attrgetter('width')).width
    rowHeight = max(image_array, key=attrgetter('height')).height
    grid = int(math.ceil(math.sqrt(numImages)))
    combinedImage = cv.CreateImage((colWidth * grid, rowHeight * grid), 8, 3)
    cv.Set(combinedImage, cv.CV_RGB(50, 50, 50))

    for index, img in enumerate(image_array):
        if img.nChannels == 1:
            colourImg = cv.CreateImage((img.width, img.height), 8, 3)
            cv.CvtColor(img, colourImg, cv.CV_GRAY2RGB)
            img = colourImg

        row = index % grid
        column = int(math.ceil(index / grid))
        cv.SetImageROI(
            combinedImage, (row * colWidth, column * rowHeight, img.width, img.height))
        cv.Copy(img, combinedImage)
        cv.ResetImageROI(combinedImage)

    return combinedImage


def read_img_cv2(img_dir):
    cv2_img_li = []
    for i in os.listdir(img_dir):
        suffix = i.split(".")
        endswich = suffix[-1]
        if endswich == "jpg":
            cv2_img = cv2.imread(img_dir + "/" + i)
            cv2_img_li.append(cv2_img)
    return cv2_img_li


def read_img_cv(img_dir):
    cv_img_li = []
    check_img_li = os.listdir(img_dir)

    img_li = []
    for i in check_img_li:
        suffix = i.split(".")
        endswich = suffix[-1]
        if endswich == "jpg":
            img_li.append(i)

    img_li.sort(key=lambda x: int(x[:-4]))
    for i in img_li:
        cv_img = cv.LoadImage(img_dir + "/" + i)
        cv_img_li.append(cv_img)
    return cv_img_li
#

def output_cv_img(src_img):

    if os.path.exists("comb_output"):
        os.system('rm -r comb_output')
        print "delete comb_output"
    os.system('mkdir comb_output')

    output_dir = "comb_output/comb.jpg"
    cv.SaveImage(output_dir, src_img)


def output_cv2_img(src_img, f_name):

    if os.path.exists("random_output"):
        os.system('rm -r random_output')
        print "delete random_output"
    os.system('mkdir random_output')

    output_dir = "random_output/" + f_name
    cv2.imwrite(output_dir, img)


def output_random_img():
    output_folder = "random_output"
    input_folder = "split_output"
    if os.path.exists(input_folder):
        cv2_img_li = read_img_cv2(input_folder)
        check_folder_exits(output_folder)
        random_order = gen_random_order(len(cv2_img_li))
        index = 0
        for img in cv2_img_li:
            f_name = repr(random_order[index])
            sufix = ".jpg"
            op_name = output_folder + "/" + f_name + sufix
            # print op_name
            cv2.imwrite(op_name, img)
            index += 1
    else:
        print "split_output folder not exist"


def output_solu_img(solutions, piece_obj_list):
    folder = "solu_output"
    cv_img_li = read_img_cv("random_output")
    check_folder_exits(folder)

    img_orders = []
    for i in solutions:
        img_order = order_to_index(i.order_list, piece_obj_list)
        img_orders.append(img_order)

    out_id = 0
    for order in img_orders:
        # print order
        count = 0
        img_indexs = []
        for img in cv_img_li:
            # cv.ShowImage("img", img)
            # cv.WaitKey()
            # cv.DestroyAllWindows()
            img_index = ImgIndex(order[count], img)
            img_indexs.append(img_index)
            count += 1

        s = sorted(img_indexs, key=lambda img_index: img_index.img_index)

        img_li = []
        for i in s:
            img_li.append(i.img)
            # print i.img_index
            # cv.ShowImage("img", i.img)
            # cv.WaitKey()
            # cv.DestroyAllWindows()

        out_id += 1
        out_img = combine_image(img_li)
        op = "solu_output" + "//" + repr(out_id) + ".jpg"
        cv.SaveImage(op, out_img)

        # cv.ShowImage("img", out_img)
        # cv.WaitKey()
        # cv.DestroyAllWindows()


def check_folder_exits(folder):
    if os.path.exists(folder):
        cmd = 'rm -r ' + folder
        os.system(cmd)
        print "delete exists folder"
    cmd = 'mkdir ' + folder
    os.system(cmd)


def gen_random_order(length):
    rnd_li = []
    for i in range(length):
        rnd_li.append(i)
    random.shuffle(rnd_li)
    return rnd_li


def gen_order_list(x, y):
    pos_li = []
    for i in range(x):
        for j in range(y):
            pos = [i, j]
            pos_li.append(pos)
    return pos_li


def load_solution(solution_sol):
    f = open(solution_sol, "rb")
    solutions = []
    while 1:
        try:
            i = pickle.load(f)
            solutions.append(i)
        except EOFError:
            print "load done..."
            return solutions
    return solutions


def progressbar(it, prefix="", size=60):
    count = len(it)

    def _show(_i):
        x = int(size * _i / count)
        sys.stdout.write("%s[%s%s] %i/%i\r" %
                         (prefix, "#" * x, "." * (size - x), _i, count))
        sys.stdout.flush()

    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i + 1)
    sys.stdout.write("\n")
    sys.stdout.flush()
