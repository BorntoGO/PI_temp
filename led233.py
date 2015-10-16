# -*- coding:utf-8 -*-
__author__ = 'Kyle Yuan'
#功能是通过手机输入'R/B',控制红灯亮或者绿灯亮,同时返回给手机当前两个灯的状态.
#后面想模拟红绿灯循环,同时行人优先,手机端相当于绿灯按钮.蛋是红绿灯循环和接收指令循环两个关系还没解决.

import RPi.GPIO as GPIO
import serial
#import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
lry = [23,24]
#channel23:绿灯,channel24红灯
GPIO.setup(lry,GPIO.OUT)

def loop():
    while True:
        iin = ser.read()

        if iin == 'B':
            #手机端输入'B'则把绿灯点亮红灯关掉,也就是23HIGH,24LOW.
            GPIO.output(lry, (1, 0))
            print 'BLUE'
        elif iin == 'R':
            #手机端输入'R'则把绿灯关掉红灯点亮,也就是23LOW,24HIGH.
            GPIO.output(lry, (0, 1))
            print 'RED'

        #读取当前23,24的值,显示给手机.
        blue = GPIO.input(23)
        red = GPIO.input(24)
        i = '\n BLUE=%d, RED=%d' % (blue, red)
        ser.write(i)

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyAMA0', 9600)
    try:
        loop()
    except KeyboardInterrupt:
        ser.close()
        GPIO.cleanup(lry)
print '实得分数电风扇'