#!/usr/bin/python
import Adafruit_DHT
from time import sleep
import time
import RPi.GPIO as GPIO
from time import localtime
import math

sensor = Adafruit_DHT.DHT22
pinsensor = 4
pinrele = 19

f1 = range(19, 24)                      #
f2 = range(0, 13)                       #
luce = not(localtime()[3] in (f1 + f2)) #
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


umi, t = Adafruit_DHT.read_retry(sensor, pinsensor, 1)
i = 0
while i < 4:
	if t is not None:
		ur = 100*(-0.9/(0.6108*math.exp(17.27*t/(t+237.3)))+1)
		min = ur - 0.2
		max = ur + 1.2
		ming = ur - 0.4
		maxg = ur + 1.4		
		i = 4
	else:
		umi, t = Adafruit_DHT.read_retry(sensor, pinsensor, 1)
		print ('la temperatura e None, riprovo altre '+repr(4-i-1)+' volte.')
		i = i + 1

#print min 
#print max

if luce == 1 and i == 4:
	if umi > max and umi < 100 and umi is not None:
				GPIO.setup(pinrele, GPIO.OUT)
				GPIO.output(pinrele, GPIO.LOW)
				print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
				print('Umidita maggiore di ideale a VPD = 9, asprazione ON')
	elif umi < min and umi is not None:
				GPIO.setup(pinrele, GPIO.OUT)
				GPIO.output(pinrele, GPIO.HIGH)
				print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
				print('Umidita minore di ideale a VPD = 9, asprazione OFF')
	elif umi >= min and umi <= max and umi is not None:
        	                print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                	        print('Umidita corretta a VPD = 9, asprazione inalterata')
	elif umi < 0 and umi > 100 and umi is not None:
				GPIO.setup(pinrele, GPIO.OUT)
				GPIO.output(pinrele, GPIO.HIGH)
				print('Il sensore ha dei problemi esce dal range 0-100*, aspirazione OFF')
	else:
				GPIO.setup(pinrele, GPIO.OUT)
				GPIO.output(pinrele, GPIO.HIGH)
				print('Il sensore la ha scialata, aspirazione OFF')
elif luce == 0 and i == 4:
        if umi > maxg and umi < 100 and umi is not None:
                                GPIO.setup(pinrele, GPIO.OUT)
                                GPIO.output(pinrele, GPIO.LOW)
                                print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                                print('Umidita maggiore di ideale a VPD = 9, asprazione ON')
        elif umi < ming and umi is not None:
                                GPIO.setup(pinrele, GPIO.OUT)
                                GPIO.output(pinrele, GPIO.HIGH)
                                print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                                print('Umidita minore di ideale a VPD = 9, asprazione OFF')
        elif umi >= ming and umi <= maxg and umi is not None:
                                print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                                print('Umidita corretta a VPD = 9, asprazione inalterata')
        elif umi < 0 and umi > 100 and umi is not None:
                                GPIO.setup(pinrele, GPIO.OUT)
                                GPIO.output(pinrele, GPIO.HIGH)
                                print('Il sensore ha dei problemi esce dal range 0-100*, aspirazione OFF')
        else:
                                GPIO.setup(pinrele, GPIO.OUT)
                                GPIO.output(pinrele, GPIO.HIGH)
                                print('Il sensore la ha scialata, aspirazione OFF')
