import os

#adb 命令 测试
face="uface"
face=face+'.png'

os.system('adb devices')
os.system('adb shell screencap -p /sdcard/'+face)
os.system('adb pull /sdcard/'+face)

 