# -*- coding:utf-8 -*-
__author__ = 'Kyle Yuan'

print 'test'

import serial

def loop():
    while True:
        i = raw_input()
        ser.write(i)

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyAMA0', 9600)
    try:
        loop()
    except KeyboardInterrupt:
        ser.close()
print "just a test"