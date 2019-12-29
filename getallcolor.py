import serial
import os

from colordetect import getfacecolor


#由串口发送的两类数据  1. 'C:' 开头 控制 命名 用于得到六面时 的控制
#                     2. 'S:' 开头 解法 用于发送最终的解法
colordict={'W':'U','Y':'D','R':'L','O':'R','B':'F','G':'B'}


def getImg(comnum="com5",baudrate=115200):

    ctrl_str='C:'
    # URFDLB 
    facelist=('f','l','r','u','d','b')
    ser=serial.Serial(comnum,baudrate,timeout=0.5)

    for face in facelist:
        sendstr=ctrl_str+face+"\r\n"
        ser.write(sendstr.encode())

        print("开始获取 %s 图像" % face)

        #等待下位机返回yes
        rec=ser.readline()
        while rec.decode()!='yes':
            rec=ser.readline()

        #下位机返回数据后 进行截图
        
        imgname=face+'.png'
        os.system('adb shell screencap -p /sdcard/'+imgname)
        os.system('adb pull /sdcard/'+imgname)
        print(face,"完成截图")

    ser.close()


def getcolor():
    allcolor=''
    color=''
    facelist=('u','r','f','d','l','b')
    for name in facelist:
        colorlist=getfacecolor(name)
        print(colorlist)
        allcolor=allcolor+''.join(colorlist)

    for a in allcolor:
        color=color+colordict[a]

    return color







