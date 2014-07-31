#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import cv2
import numpy as np

#read image
img = cv2.imread("cat.jpg")

#display window name
cv2.namedWindow("Image")

#
emptyImage = np.zeros(img.shape, np.uint8)
print emptyImage.__array__
#copy image
emptyImage2 = img.copy()

#
emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print 
# emptyImage3[...]=0 

#show image
cv2.imshow("Image", emptyImage3)

#wait any a key event ,0 is mean forever
cv2.waitKey (0)
# cv2.destroyAllWindows()

#save image
cv2.imwrite("cat2.jpg", emptyImage3, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
# print emptyImage3
