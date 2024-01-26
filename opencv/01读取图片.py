# cv模块
import cv2 as cv
# 读取图像
img = cv.imread('D:\\python\\opencv\\face2.jpg')
# 显示图像
cv.imshow('Image', img)
while True:
    if ord('q') == cv.waitKey(0):
        break
# 等待
cv.waitKey(0)
# 释放内存
cv.destroyAllWindows()