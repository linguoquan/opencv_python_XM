import cv2
import numpy as np

img = np.zeros((512, 512, 3), dtype=np.uint8)
# img: 图像，要在其上绘制圆形的图像。
# center: 圆心坐标。
# radius: 圆的半径。
# color: 圆的颜色，通常是一个BGR元组。
# thickness: 线条的宽度为整数值，如果为 - 1表示填充圆。
# lineType: 线条的类型，可以是
# cv2.LINE_4、cv2.LINE_8
# 或
# cv2.LINE_AA。
# shift: 像素坐标点的小数部分位数。

# cv2.circle(img, (250, 250), 150, (0, 0, 255), -1)
cv2.circle(img, (250, 250), 150, (0, 0, 255), 4,10)
cv2.imshow('Circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
