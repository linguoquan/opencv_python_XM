import cv2
import numpy as np
'''

画线、圈、文字
画线 建一个全黑的矩阵
'''
img=np.zeros((512,512,3),np.uint8)
#print(img) high width
#img[200:300,100:300]=255,0,0

#1.line 画线
#             起点    终点      颜色
cv2.line(img,(0,0),(300,300),(0,255,0),3)
#img.shape[1] high  img.shape[0] width
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

#2.画矩形 起点 终点 颜色 线条(填充)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)

#3.画圈 400,50 圆心的位置
cv2.circle(img,(400,50),30,(255,255,0),5)
#4.输出 文字 字体  颜色
cv2.putText(img,"OPENCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0))

cv2.imshow("Image",img)
cv2.waitKey(0)
