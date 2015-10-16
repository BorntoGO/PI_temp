# -*- coding:utf-8 -*-
__author__ = 'Kyle Yuan'

<<<<<<< HEAD
print 'test'
print 'temp'

=======
>>>>>>> 64e211db23a29a4667fdd1c1d18768a9dd2ca4ee
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
<<<<<<< HEAD
print "测x试"
=======
print "测试"
>>>>>>> 64e211db23a29a4667fdd1c1d18768a9dd2ca4ee
