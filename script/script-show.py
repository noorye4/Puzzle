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
solutions = load_solution(input_sol)
output_solu_img(solutions)
