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

try:
#	umi, t = Adafruit_DHT.read_retry(sensor, pinsensor)

	if t is not None and t < 22:
		
		GPIO.output(pinrele, GPIO.LOW)
		print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
	elif t is not None and t > 23:
                GPIO.output(pinrele, GPIO.HIGH)
                print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
	elif t is not None and t >= 22 and t <= 23:
                print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
	else:
     		print('Il sensore la ha scialata')

except KeyboardInterrupt:
	raise
        print("Interrotto")

sleep(sleepTime)
