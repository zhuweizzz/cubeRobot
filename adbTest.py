import os


os.system('adb devices')
os.system('adb shell screencap -p /sdcard/screen.png')
os.system('adb pull /sdcard/screen.png')

