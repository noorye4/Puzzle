#/usr/bin/env python
#-*- encoding: utf-8 -*-
import os
import time
import cv

os.system("python script-split.py ../image/cat.jpg 3 3")
os.system("python script-random.py")
os.system("python script-combine.py random_output")

# cv_img = cv.LoadImage("comb_output/comb.jpg")
# cv.ShowImage("img", cv_img)
# cv.WaitKey()
# cv.DestroyAllWindows()
time.sleep(2)

os.system("python script-puzzle.py random_output 3 3 cat")
os.system("python script-show.py cat.sol")

