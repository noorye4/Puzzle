import cv2
import numpy as np

img = cv2.imread("cat.jpg")
b, g, r = cv2.split(img)
print r
#cv2.imshow("Blue", r)
#cv2.imshow("Red", g)
#cv2.imshow("Green", b)
cv2.waitKey(0)
cv2.destroyAllWindows()
