import os
import random

#third party library
import cv
import cv2
import numpy as np

#puzzle library
from puzzle2 import *
from basic import *
from itertools import *



# src = gen_order_list(3, 3)
# src = [(0,0),(0,1),(1,0),(1,1)]
src = [0,1,2,3]



# for i in src:
    # print i
# x = list(permutations(li))

# x = set(x)
# print len(x)


src = [1, 2, 3]

src =  (permutations(src,len(src)))



for i in src:
    print i

