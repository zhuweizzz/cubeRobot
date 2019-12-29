import getallcolor
import kociemba
import serial

import serial.tools.list_ports

#用字符 H   I   J   X   Y   Z
#  代替 U2  R2  F2  D2  L2  B2
actlist=["U2","U'","R2","R'","F2","F'","D2","D'","L2","L'","B2","B'"]
actdict={"U2":'H',"U'":'u',"R2":'I',"R'":'r',"F2":'J',"F'":'f',"D2":'X',"D'":'d',"L2":'Y',"L'":'l',"B2":'Z',"B'":'b'}

#查询可用串口
port_list = list(serial.tools.list_ports.comports())

if len(port_list) == 0:
   print('无可用串口')
else:
    for i in range(0,len(port_list)):
        comnum=port_list[i].device
        print('串口 %s 已打开' % comnum)


# 'f','l','r','u','d','b'
getallcolor.getImg(comnum)  #从摄像头中截取图片
colorlist=getallcolor.getcolor() #图像处理得到颜色
print(colorlist)
solve=kociemba.solve(colorlist)  # 得到解法

#由串口发送的两类数据  1. 'C:' 开头 控制 命名 用于得到六面时 的控制
#                     2. 'S:' 开头 解法 用于发送最终的解法

sendstr='S:'

#对返回的解法字符串进行处理
for act in actlist:
    temp=solve.replace(act,actdict[act])
    solve=temp

solve=solve.replace(" ","")

#将处理后的字符串发送
sendstr=sendstr+solve

print(sendstr)

sendstr=sendstr+'\r\n'

ser=serial.Serial(comnum,115200,timeout=0.5)
ser.write(sendstr.encode())

print('解法发送完成')






























