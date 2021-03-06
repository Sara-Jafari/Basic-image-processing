import cv2
import numpy as np


img1 = cv2.imread("6.jpg")
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

corners=cv2.goodFeaturesToTrack(gray,200,0.1,10)
corners=np.int0(corners)

for corner in corners:
    x ,y =corner.ravel()
    cv2.circle(img1,(x , y),3,(0.,0,255),1)

cv2.imshow("frame", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
