import serial


import serial.tools.list_ports
port_list = list(serial.tools.list_ports.comports())

if len(port_list) == 0:
   print('无可用串口')
else:
    for i in range(0,len(port_list)):
        comnum=port_list[i].device

 
ser=serial.Serial(comnum,115200,timeout=0.5)
print("打开串口")
print(ser.name)

a="yes"
a=a+"\r\n"

ser.write(a.encode())

rec=ser.readline()
while rec.decode()!='yes':
    rec=ser.readline()

print(rec.decode())

rec=ser.readline()

print(rec)

