import Adafruit_DHT
from time import sleep
import time
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT22
pinsensor = 4
sleepTime = 3
pinrele = 13
umi, t = Adafruit_DHT.read_retry(sensor, pinsensor)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinrele, GPIO.OUT)
min = 22
max = 23

try:
#	umi, t = Adafruit_DHT.read_retry(sensor, pinsensor)

	if t < min:
		GPIO.output(pinrele, GPIO.LOW)
		print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
	elif t > max:
                GPIO.output(pinrele, GPIO.HIGH)
                print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
	elif t >= min and t <= max:
                print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
	elif t is None:
	   	GPIO.output(pinrele, GPIO.HIGH)
           	print('Il sensore la ha scialata')
	elif t < 0:
		GPIO.output(pinrele, GPIO.HIGH)
		print('Il sensore ha dei problemi esce dal range 0-50C*')
	else:
     		print('Il sensore la ha scialata')

except KeyboardInterrupt:
	raise
        print("Interrotto")

sleep(sleepTime)
