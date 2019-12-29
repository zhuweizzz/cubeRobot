import cv2
import numpy as np

import os

#adb 命令 测试

# os.system('adb devices')
# os.system('adb shell screencap -p /sdcard/screen.png')
# os.system('adb pull /sdcard/screen.png')

#找到魔方的中心点
def findPoint(src):
    loc1 = [0, 0]
    loc2 = [0, 0]

    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    dst = cv2.bilateralFilter(src, 8, 16, 5)
    dst = cv2.Canny(dst, 60, 70)

    [H, W] = src.shape[0:2]

    for row in range(0, int(H*0.25), 3):
        for col in range(0, int(W*0.25), 10):
            if dst[row][col] == 255:
                loc1[0] = row
                loc1[1] = col
                break
        if dst[loc1[0], loc1[1]] == 255:
            break

    for row in range(H-1, int(H*0.75), -3):
        for col in range(W-1, int(W*0.75), -10):
            if dst[row][col] == 255:
                loc2[0] = row
                loc2[1] = col
                break
    return (int((loc1[0]+loc2[0])/2), int((loc1[1]+loc2[1])/2))

#根据HSV值确定色块颜色
def checkColor(HSVval):
    print(HSVval)
    if ((HSVval[0] >= 1 and HSVval[0] <= 15) and (HSVval[1] >= 43 and HSVval[1] <= 255) and (HSVval[2] >= 210 and HSVval[2] <= 255)):
        return 'O'
    elif (((HSVval[0] >= 0 and HSVval[0] <= 85) or (HSVval[0] >= 130 and HSVval[0] <= 180)) and (HSVval[1] >= 150 and HSVval[1] <= 240) and (HSVval[2] >= 110 and HSVval[2] <= 220)):
        return 'R'
    elif ((HSVval[0] >= 40 and HSVval[0] <= 80) and (HSVval[1] >= 180 and HSVval[1] <= 255) and (HSVval[2] >= 50 and HSVval[2] <= 230)):
         return 'B'
    elif ((HSVval[0] >= 0 and HSVval[0] <= 180) and (HSVval[1] >= 0 and HSVval[1] <= 165) and (HSVval[2] >= 180 and HSVval[2] <= 250)):
        return 'W'
    elif ((HSVval[0] >= 25 and HSVval[0] <= 65) and (HSVval[1] >= 185 and HSVval[1] <= 255) and (HSVval[2] >= 150 and HSVval[2] <= 255)):
        return 'G'
    elif ((HSVval[0] >= 15 and HSVval[0] <= 30) and (HSVval[1] >= 145 and HSVval[1] <= 240) and (HSVval[2] >= 90 and HSVval[2] <= 255)):
        return 'Y'
    else:
        return 'N'

#取色块内8个点取平均值
def get8map(HSVmap, heart=(0, 0)):
    sumfloor=[0,0,0]
    for floor in range(0,3,1):
        for i in range(-4, 5, 4):
            for j in range(-4, 5, 4):
                sumfloor[floor] = sumfloor[floor]+HSVmap[floor][heart[1]+i][heart[0]+j]
        sumfloor[floor]=int(sumfloor[floor]/9)
    return sumfloor


#得到一个面的颜色
def getcolor(matHsv, locList):
    colorList = []
    hsvmap = cv2.split(matHsv)
    for i in range(0, 9, 1):
        colorList.append(checkColor(get8map(hsvmap,locList[i])))
    return colorList

def getloc(width,selfpoint=(0,0)):
    locList = []
    locList.append((selfpoint[0]-width, selfpoint[1]-width))  # 1
    locList.append((selfpoint[0], selfpoint[1]-width))  # 2
    locList.append((selfpoint[0]+width, selfpoint[1]-width))  # 3

    locList.append((selfpoint[0]-width, selfpoint[1]))  # 4
    locList.append((selfpoint[0], selfpoint[1]))  # 5
    locList.append((selfpoint[0]+width, selfpoint[1]))  # 6

    locList.append((selfpoint[0]-width, selfpoint[1]+width))  # 7
    locList.append((selfpoint[0], selfpoint[1]+width))  # 8
    locList.append((selfpoint[0]+width, selfpoint[1]+width))  # 9

    return  locList

def getfacecolor(facename):

    y0=478
    y1=957
    x0=361
    x1=840

    Source = cv2.imread(facename+'.png')
    sourceQuite = Source[y0:y1, x0:x1]  # 对读取的图片裁剪
    cv2.imshow('1',sourceQuite)
    x, y = sourceQuite.shape[0:2]   #得到裁剪后图片的大小
    cubeImg = cv2.resize(sourceQuite, (int(y/3), int(x/3)))  # 对读取的图片进行裁剪
    cv2.imshow('2',cubeImg)
    #selfpoint = findPoint(cubeImg)

    width=int((y1-y0)/9)-5
    selfpoint=(int((x1-x0)/6),int((y1-y0)/6))

    locList=getloc(width,selfpoint)

    cv2.circle(cubeImg, selfpoint, 5, (0, 0, 255), -1)
    cv2.circle(cubeImg, locList[0], 5, (0, 0, 255), -1)
    cv2.circle(cubeImg, locList[1], 5, (0, 0, 255), -1)
    cv2.circle(cubeImg, locList[2], 5, (0, 0, 255), -1)
    cv2.circle(cubeImg, locList[3], 5, (0, 0, 255), -1)
    cv2.circle(cubeImg, locList[5], 5, (0, 0, 255), -1)
    cv2.circle(cubeImg, locList[6], 5, (0, 0, 255), -1)
    cv2.circle(cubeImg, locList[7], 5, (0, 0, 255), -1)
    cv2.circle(cubeImg, locList[8], 5, (0, 0, 255), -1)

    cv2.imshow('3',cubeImg)
    
    cubeHsv = cv2.cvtColor(cubeImg, cv2.COLOR_BGR2HSV)

    # hsvsplit=cv2.split(cubeHsv)
    # hsvsplit[0]=cv2.equalizeHist(hsvsplit[0])
    # cubeHsv=cv2.merge(hsvsplit)


    colorList=getcolor(cubeHsv,locList)

    return colorList

# colorlist=getfacecolor('screen')
# print(colorlist)
# cv2.waitKey(10000)