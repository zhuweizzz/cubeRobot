import os

#adb 命令 测试

os.system('adb devices')
os.system('adb shell screencap -p /sdcard/screen.png')
os.system('adb pull /sdcard/screen.png')

