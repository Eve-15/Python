# cv模块
import cv2 as cv
# 读取图片
img = cv.imread('D:\\python\\opencv\\face2.jpg')
# 灰度转换
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 显示灰度图片
cv.imshow('gray',gray_img)
# 保存灰度图片
cv.imwrite('gray_face11.jpg',gray_img)
# 显示图片
cv.imshow('Image', img)
# 等待
cv.waitKey(0)
# 释放内存
cv.destroyAllWindows()