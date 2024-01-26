# cv模块
import cv2 as cv
# 读取图像
img = cv.imread('D:\\python\\opencv\\face2.jpg')
# 修改尺寸
resize_img = cv.resize(img,dsize = (200,200))
# 显示原图
cv.imshow('Image', img)
# 修改后的图片
cv.imshow('resize_img', resize_img)
# 打印原图大小
print('原图大小',img.shape)
# 打印修改后的大小
print('修改后大小',resize_img.shape)
# 等待
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()