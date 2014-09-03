import os
import random

#third party library
import cv
import cv2
import numpy as np

#puzzle library
from puzzle2 import *
from basic import *



li = gen_order_list(3, 3)

print li
print "-"*30
random.shuffle(li)

print li
print "-"*30
li.sort()
print li

