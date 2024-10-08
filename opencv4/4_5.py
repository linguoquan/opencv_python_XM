import cv2
import numpy as np

img = np.zeros((512, 512, 3), dtype=np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 300), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('Text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
