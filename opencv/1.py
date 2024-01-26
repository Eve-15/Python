import cv2 as cv

# 加载训练数据集文件
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('D:/python/opencv/trainer.yml')

# 准备识别的照片
img = cv.imread('D:/python/opencv/4.name.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 使用人脸级联分类器进行人脸检测
face_detector = cv.CascadeClassifier('C:/Users/Lenovo/Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
faces = face_detector.detectMultiScale(gray)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # 进行人脸识别
    id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
    print('标签id:', id, '置信评分:', confidence)
    
    if confidence > 80:
        cv.putText(img, 'Unknown', (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    else:
        cv.putText(img, 'U', (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)

cv.imshow('result', img)
cv.waitKey(0)

