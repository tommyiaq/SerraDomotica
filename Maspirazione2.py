import Adafruit_DHT
from time import sleep
import time
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT22
pinsensor = 4
sleepTime = 60
pinrele = 19
umi, t = Adafruit_DHT.read_retry(sensor, pinsensor)
min = 70.0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.setup(pinrele, GPIO.OUT, initial = 1)

if umi > min and umi < 100 and umi is not None:
		GPIO.setup(pinrele, GPIO.OUT)
		GPIO.output(pinrele, GPIO.LOW)
		print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
		print('Umidita magiore di min , asprazione ON')
		sleep(sleepTime)
elif umi < min and umi is not None:
                GPIO.setup(pinrele, GPIO.OUT)
		GPIO.output(pinrele, GPIO.HIGH)
                print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                print('Umidita minore di min, asprazione OFF')
elif umi < 0 and umi > 100 and umi is not None:
                GPIO.setup(pinrele, GPIO.OUT)
		GPIO.output(pinrele, GPIO.HIGH)
		print('Il sensore ha dei problemi esce dal range 0-100*')
else:
                GPIO.setup(pinrele, GPIO.OUT)
                GPIO.output(pinrele, GPIO.HIGH)
		print('Il sensore la ha scialata, aspirazione OFF')
GPIO.cleanup()
