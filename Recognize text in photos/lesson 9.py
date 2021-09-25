import cv2
import numpy as np

img1 = cv2.imread("37.jpg")



gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,threshold = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow("frame1", img1)
cv2.imshow("frame2", threshold)
cv2.imshow("frame3", th)
cv2.waitKey(0)
cv2.destroyAllWindows()
