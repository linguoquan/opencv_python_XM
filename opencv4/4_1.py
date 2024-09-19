import cv2
import numpy as np

img=np.zeros((640,640,3),np.uint8)

# 画线，坐标为（x,y)参数结束
# img：在那个图像上画线
# 开始点,结束点：指定线的开始与结束位置；
# 颜色，线宽，线体
cv2.line(img,(0,0),(640,640),(0,0,255),5,30)
# cv2.line(img,(80,100),(320,420),(0,0,255),5,16)

cv2.imshow('line',img)
cv2.waitKey(0)

