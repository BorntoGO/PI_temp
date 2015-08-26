# -*- coding:utf-8 -*-
__author__ = 'Kyle Yuan'

import serial

def loop():
    while True:
        # i = ser.read()
        i = ser.readline()
        # read a '\n' terminated line
        print i

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyAMA0', 9600)
    try:
        loop()
    except KeyboardInterrupt:
        ser.close()
