import serial

ser=serila.serial('com5','115200',timeout=0.5)
ser.

def serialopen(comnum='com5',baudrate=115200):
    ser=serial.serial(comnum,baudrate,timeout=0.5)
    print(comnum)
    print('已打开')

def serialclose():


def serialSend(sendstr,comnum='com5',baudrate=115200):
    ser=serial.Serial(comnum,baudrate,timeout=0.5)
    print('打开串口:' )
    print(ser.name)
    sendstr=sendstr + '\r\n'
    ser.write(sendstr.encode)
    ser.close()
    print('发送完毕')

def serialrecevie():



