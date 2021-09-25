import cv2
import numpy as np

img1 = cv2.imread("i1.jpg")
img2 = cv2.imread("2.jpg")

#add = img1 + img2
#add=cv2.add(img1,img2)
add=cv2.addWeighted(img1,0.1,img2,0.7,0)
cv2.imshow("add" ,add)
cv2.waitKey(0)
cv2.destroyAllWindows()