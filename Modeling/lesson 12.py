import cv2
import numpy as np


img_asli = cv2.imread("4.jpg")
img_gray = cv2.cvtColor(img_asli,cv2.COLOR_BGR2GRAY)

img_template = cv2.imread("5.jpg",0)
w ,h =img_template.shape[::-1]
res = cv2.matchTemplate(img_asli,img_template,cv2.TM_CCOEFF_NORMED,None,None)
threshhold=0.8
loc=np.where(res >=threshhold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_asli,pt,(pt[0]+w),(pt[1],h),(0,0,255),1)

cv2.imshow("frame1", img_asli)
cv2.waitKey(0)
cv2.destroyAllWindows()

