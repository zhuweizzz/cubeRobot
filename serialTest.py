import serial

ser=serial.Serial("com5",115200,timeout=0.5)
print("打开串口")
print(ser.name)

a="asdsdasdsd"
a=a+"\r\n"

ser.write(a.encode())

rec=ser.read(16)
ser.close()


print(rec)


