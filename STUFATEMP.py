import Adafruit_DHT
from time import sleep
import time
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT22
pinsensor = 4
sleepTime = 3
pinrele = 26
umi, t = Adafruit_DHT.read_retry(sensor, pinsensor)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinrele, GPIO.OUT)
GPIO.output(pinrele, GPIO.HIGH)


while True:
	umi, t = Adafruit_DHT.read_retry(sensor, pinsensor)

	if t is not None and t < 22:
		GPIO.output(pinrele, GPIO.LOW)
		print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
	elif t is None:
		print("Il sensore l'ha scialata")
	else:
		GPIO.output(pinrele, GPIO.HIGH)
		print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
sleep(sleepTime)
