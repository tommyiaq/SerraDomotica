#!/usr/bin/python
import Adafruit_DHT
from time import sleep
import time
import RPi.GPIO as GPIO
from time import localtime

sensor = Adafruit_DHT.DHT22
pinsensor = 4
sleepTime = 60
sleepTimeG = 22
pinrele = 19
umi, t = Adafruit_DHT.read_retry(sensor, pinsensor)
min = 70.0
minG = 68.0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

f1 = range(19, 24)
f2 = range(0, 13)
luci = not(localtime()[3] in (f1 + f2))
#print localtime()[3]
#print luci

if luci == 1:
	if umi > min and umi < 100 and umi is not None:
			GPIO.setup(pinrele, GPIO.OUT)
			GPIO.output(pinrele, GPIO.LOW)
			print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
			print('Umidita maggiore di min notturna , asprazione ON','luci='+repr(luci))
	elif umi < min-4 and umi is not None:
			GPIO.setup(pinrele, GPIO.OUT)
			GPIO.output(pinrele, GPIO.HIGH)
			print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
			print('Umidita minore di min notturno, asprazione OFF','luci='+repr(luci))
	elif umi >= min-4 and umi < min and umi is not None:
                        print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Umidita notturno corretta, asprazione inalterata','luci='+repr(luci))
	elif umi < 0 and umi > 100 and umi is not None:
			GPIO.setup(pinrele, GPIO.OUT)
			GPIO.output(pinrele, GPIO.HIGH)
			print('Il sensore ha dei problemi esce dal range 0-100*, aspirazione OFF')
	else:
			GPIO.setup(pinrele, GPIO.OUT)
			GPIO.output(pinrele, GPIO.HIGH)
			print('Il sensore la ha scialata, aspirazione OFF')
elif luci == 0:
	if umi > minG and umi < 100 and umi is not None:
                        GPIO.setup(pinrele, GPIO.OUT)
                        GPIO.output(pinrele, GPIO.LOW)
                        print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Umidita maggiore di min diurna , asprazione ON','luci='+repr(luci))
        elif umi < minG-5 and umi is not None:
                        GPIO.setup(pinrele, GPIO.OUT)
                        GPIO.output(pinrele, GPIO.HIGH)
                        print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Umidita minore di min diurna, asprazione OFF','luci='+repr(luci))
        elif umi >= minG-5 and umi is not None:
                        print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Umidita diurna corretta, asprazione inalterata','luci=',repr(luci))
        elif umi < 0 and umi > 100 and umi is not None:
                        GPIO.setup(pinrele, GPIO.OUT)
                        GPIO.output(pinrele, GPIO.HIGH)
                        print('Il sensore ha dei problemi esce dal range 0-100*, aspirazione OFF')
        else:
                        GPIO.setup(pinrele, GPIO.OUT)
                        GPIO.output(pinrele, GPIO.HIGH)
                        print('Il sensore la ha scialata, aspirazione OFF')

