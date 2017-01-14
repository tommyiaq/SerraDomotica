import Adafruit_DHT
from time import sleep
import time
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT22
pinsensor = 4
sleepTime = 3
pinrele = 13
pinrele2 = 26
pinventi = 6
umi, t = Adafruit_DHT.read_retry(sensor, pinsensor, 5, 1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinrele, GPIO.OUT)
GPIO.setup(pinrele2, GPIO.OUT)
GPIO.setup(pinventi, GPIO.OUT)

luce = GPIO.input(pinrele2)
venti = GPIO.input(pinventi)
min = 22
max = 22.5

minN = 19
maxN = 19.5
i = 0

while i < 1:
	if luce == 0 and luce is not None:	 
		if t < min and t is not None:
			GPIO.output(pinrele, GPIO.LOW)
			GPIO.output(pinventi, GPIO.HIGH)
			print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Temperatura diurna bassa, stufa ON, luci='+repr(luce)+', ventilatore='+repr(venti))
			i = 1
		elif t > max and t is not None:
	                GPIO.output(pinrele, GPIO.HIGH)
                        if t > max+1.7:
				GPIO.output(pinventi, GPIO.LOW)
			elif t < max+1.6:
	                        GPIO.output(pinventi, GPIO.HIGH)
			print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Temperatura diurna alta, stufa OFF, luci='+repr(luce)+', ventilatore='+repr(venti))
			i = 1
		elif t >= min and t <= max and t is not None:
                        GPIO.output(pinventi, GPIO.HIGH)
        	        print ('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Temperatura diurna OK, stufa OFF, luci='+repr(luce)+', ventilatore='+repr(venti))
			i = 1	
		elif t is None:
                        GPIO.output(pinventi, GPIO.HIGH)
		   	GPIO.output(pinrele, GPIO.HIGH)
           		print('Il sensore la ha scialata, None')
	                umi, t = Adafruit_DHT.read_retry(sensor, pinsensor, 5, 1)
		elif t < 0 and t > 50:
                        GPIO.output(pinventi, GPIO.HIGH)
			GPIO.output(pinrele, GPIO.HIGH)
			print('Il sensore ha dei problemi esce dal range 0-50C*')
        	        umi, t = Adafruit_DHT.read_retry(sensor, pinsensor)
		else:
     			print('Il sensore la ha scialata')
               		umi, t = Adafruit_DHT.read_retry(sensor, pinsensor, 5, 1)
	elif luce == 1 and luce is not None:
                if t < minN and t is not None:
                        GPIO.output(pinrele, GPIO.LOW)
                        GPIO.output(pinventi, GPIO.HIGH)
                        print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Temperatura notturna bassa, stufa ON, luci='+repr(luce)+', ventilatore='+repr(venti))
			i = 1
		elif t > maxN and t is not None:
			 GPIO.output(pinrele, GPIO.HIGH)
                         if t > maxN+1.7:
                                GPIO.output(pinventi, GPIO.LOW)
                         elif t < maxN+1.6:
			       GPIO.output(pinventi, GPIO.HIGH)
                         print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                         print('Temperatura diurna alta, stufa OFF, luci='+repr(luce)+', ventilatore='+repr(venti))
               		 i = 1
		elif t >= minN and t <= maxN and t is not None:
                        GPIO.output(pinventi, GPIO.HIGH)
			print ('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Temperatura diurna OK, stufa OFF, luci='+repr(luce)+', ventilatore='+repr(venti))                       
               		i = 1
		elif t is None:
                        GPIO.output(pinventi, GPIO.HIGH)
                        GPIO.output(pinrele, GPIO.HIGH)
                        print('Il sensore la ha scialata, None')
	                umi, t = Adafruit_DHT.read_retry(sensor, pinsensor, 5, 1)
                elif t < 0:
                        GPIO.output(pinventi, GPIO.HIGH)
                        GPIO.output(pinrele, GPIO.HIGH)
                        print('Il sensore ha dei problemi esce dal range 0-50C*')
	                umi, t = Adafruit_DHT.read_retry(sensor, pinsensor)
                else:
                        print('Il sensore la ha scialata')
	                umi, t = Adafruit_DHT.read_retry(sensor, pinsensor, 5, 1)
	else:
		luce = GPIO.input(26)
		print ('adafruit restituisce cazzate')


#except KeyboardInterrupt:
#	raise
#        print("Interrotto")
