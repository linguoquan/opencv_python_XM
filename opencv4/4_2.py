import cv2
import numpy as np

img=np.zeros((640,640,3),np.uint8)
# 指定矩形的左上角和右下角坐标
pt1 = (100, 100)
pt2 = (400, 400)

# 指定矩形的颜色和线条粗细
color = (0, 255, 0)
thickness = 2

# 画矩形
cv2.rectangle(img, pt1, pt2, color, thickness)


cv2.imshow('line',img)
cv2.waitKey(0)
