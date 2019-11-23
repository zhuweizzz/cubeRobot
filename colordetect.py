import cv2
import numpy as np


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

    width = int((loc2[0]-loc1[0])/3)
    return width, (int((loc1[0]+loc2[0])/2), int((loc1[1]+loc2[1])/2))

#根据HSV值确定色块颜色
def checkColor(HSVval):
    if ((HSVval[0] >= 0 and HSVval[0] <= 22) and (HSVval[1] >= 43 and HSVval[1] <= 255) and (HSVval[2] >= 200 and HSVval[2] <= 255)):
        return 'O'
    elif (((HSVval[0] >= 0 and HSVval[0] <= 10) or (HSVval[0] >= 150 and HSVval[0] <= 180)) and (HSVval[1] >= 150 and HSVval[1] <= 240) and (HSVval[2] >= 100 and HSVval[2] <= 200)):
        return 'R'
    elif ((HSVval[0] >= 76 and HSVval[0] <= 130) and (HSVval[1] >= 180 and HSVval[1] <= 255) and (HSVval[2] >= 46 and HSVval[2] <= 210)):
         return 'B'
    elif ((HSVval[0] >= 0 and HSVval[0] <= 180) and (HSVval[1] >= 0 and HSVval[1] <= 20) and (HSVval[2] >= 180 and HSVval[2] <= 245)):
        return 'W'
    elif ((HSVval[0] >= 39 and HSVval[0] <= 75) and (HSVval[1] >= 185 and HSVval[1] <= 230) and (HSVval[2] >= 150 and HSVval[2] <= 255)):
        return 'G'
    elif ((HSVval[0] >= 22 and HSVval[0] <= 38) and (HSVval[1] >= 145 and HSVval[1] <= 190) and (HSVval[2] >= 90 and HSVval[2] <= 255)):
        return 'Y'
    else:
        return 'N'

#取色块内8个点取平均值
def get8map(HSVmap, heart=(0, 0)):
    sumfloor=[0,0,0]
    for floor in range(0,3,1):
        for i in range(-8, 9, 8):
            for j in range(-8, 9, 8):
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
    Source = cv2.imread(facename+'.png')
    sourceQuite = Source[430:1480, 0:1070]  # 对读取的图片裁剪
    x, y = sourceQuite.shape[0:2]
    cubeImg = cv2.resize(sourceQuite, (int(y/3), int(x/3)))  # 对读取的图片进行裁剪
    [width, selfpoint] = findPoint(cubeImg)
    locList=getloc(width,selfpoint)
    cubeHsv = cv2.cvtColor(cubeImg, cv2.COLOR_BGR2HSV)
    colorList=getcolor(cubeHsv,locList)

    return colorList