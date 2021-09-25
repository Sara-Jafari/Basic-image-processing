import cv2
import numpy as np

img = cv2.imread("i1.jpg", cv2.IMREAD_COLOR)
#img[100:200,100:200]=[155,255,255]
part1 = img[300:400, 300:400]

#img[100:200, 100:200] = part1
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


