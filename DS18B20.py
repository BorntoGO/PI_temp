# -*- coding:utf-8 -*-

import time
import requests
import json
#import glob
#import os

#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

#base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'
#print device_file

device_file = '/sys/bus/w1/devices/28-01157118a7ff/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(5)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
    return temp_c

def upload_temp():
    temp = read_temp()
    apiheaders = {'U-ApiKey': 'XXXXX', 'content-type': 'application/json'}
    apiurl = 'http://api.yeelink.net/v1.0/device/XXX/sensor/XXX/datapoints'
    upload = {'value': temp}
    requests.post(apiurl, headers=apiheaders, data=json.dumps(upload))
#    print('temp: %f' % temp)

def upload_cup_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = float(file.read()) / 1000.0
    file.close()
    apiheaders = {'U-ApiKey': 'XXXXXX', 'content-type': 'application/json'}
    apiurl = 'http://api.yeelink.net/v1.0/device/XXX/sensor/XXX/datapoints'
    upload = {'value': cpu_temp}
    requests.post(apiurl, headers=apiheaders, data=json.dumps(upload))
#    print('cpu_temp: %f' % cpu_temp)

while True:
    upload_temp()
    upload_cup_temp()
    time.sleep(1800)
print 'just a test'
print '测试'
