import cv2
import numpy as np

def nothing(x):
    pass

y0=315
y1=1182
x0=59
x1=930

Source = cv2.imread('f.png')
sourceQuite = Source[y0:y1, x0:x1]  # 对读取的图片裁剪
x, y = sourceQuite.shape[0:2]   #得到裁剪后图片的大小
cubeImg = cv2.resize(sourceQuite, (int(y/3), int(x/3)))  # 对读取的图片进行缩小
cv2.imshow('2',cubeImg)
cubeHsv = cv2.cvtColor(cubeImg, cv2.COLOR_BGR2HSV)

cv2.namedWindow('Threshold')


cv2.createTrackbar('LowH','Threshold',0,180,nothing)
cv2.createTrackbar('HighH','Threshold',0,180,nothing)

cv2.createTrackbar('LowS','Threshold',0,255,nothing)
cv2.createTrackbar('HighS','Threshold',0,255,nothing)

cv2.createTrackbar('LowV','Threshold',0,255,nothing)
cv2.createTrackbar('HighV','Threshold',0,255,nothing)

while True :
    lowH=cv2.getTrackbarPos('LowH','Threshold')
    HighH=cv2.getTrackbarPos('HighH','Threshold')

    lowS=cv2.getTrackbarPos('LowS','Threshold')
    HighS=cv2.getTrackbarPos('HighS','Threshold')

    lowV=cv2.getTrackbarPos('LowV','Threshold')
    HighV=cv2.getTrackbarPos('HighV','Threshold')

    hsvsplit=np.zeros(cubeImg.shape,np.uint8)
    #imgThresholded=np.zeros(cubeImg.shape,np.uint8)

    cv2.split(cubeHsv,hsvsplit)
    cv2.equalizeHist(hsvsplit[2],hsvsplit[2])
    cv2.merge(hsvsplit,cubeHsv)

    low=np.array([lowH,lowS,lowV])
    high=np.array([HighH,HighS,HighV])
    imgThresholded=cv2.inRange(cubeHsv,low,high)

    element=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    imgThresholded=cv2.morphologyEx(imgThresholded,cv2.MORPH_OPEN,element)

    imgThresholded=cv2.morphologyEx(imgThresholded,cv2.MORPH_CLOSE,element)

    cv2.imshow('1',imgThresholded)
    
    a=cv2.waitKey(300)
    if a == 27:
        break









