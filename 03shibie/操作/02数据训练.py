# 导入模块
import os
import cv2 as cv
from  PIL import Image
import numpy as np


def getImageAndLabels(path):
    # 储存人脸数据
    faceSamples = []
    # 存储姓名数据
    ids = []
    # 储存图片信息
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    # 加载分类器
    face_detector = cv.CascadeClassifier('C:/Users/Lenovo/Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    #打印数组imagePaths
    print('数据排列：',imagePaths)
    id=None  # 设置默认值
    # 遍历列表中的图片
    for imagePath in imagePaths:
        # 打开图片，灰度化PIL有九种不同模式：1,L,P,RGB,RGBA,CMYK,YCbCr,I,F
        PIL_img = Image.open(imagePath).convert('L')
        # 将图片转换为数组，以黑白深浅
        img_numpy = np.array(PIL_img,'uint8')
        # 获取图片人脸特征
        faces = face_detector.detectMultiScale(img_numpy)
        # 获取每张图片的id和姓名
        id = int(os.path.split(imagePath)[1].split('.')[0])
        # 预防无面容图片
        for x,y,w,h in faces:
            ids.append(id)
            faceSamples.append(img_numpy[y:y+h,x:x+w])
        # 打印脸部特征和id
    if id is not None:  # 只有当id不为None时才打印
        print('id:',id)
    print('fs:',faceSamples)
    return faceSamples,ids

if __name__ == '__main__':
    #图片路径
    path='D:\\python\\03shibie\\data\\'
    #获取图像数组和id标签数组和姓名
    faces,ids=getImageAndLabels(path)
    #获取训练对象
    recognizer=cv.face.LBPHFaceRecognizer_create()
    #recognizer.train(faces,names)#np.array(ids)
    recognizer.train(faces,np.array(ids))
    #保存文件
    recognizer.write('D:\\python\\03shibie\\data\\trainer.yml')
    #save_to_file('names.txt',names)