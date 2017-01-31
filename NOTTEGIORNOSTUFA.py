import Adafruit_DHT
from time import sleep
import time
import RPi.GPIO as GPIO
from time import localtime
import math

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
#GPIO.setup(pinrele2, GPIO.OUT)
GPIO.setup(pinventi, GPIO.OUT)
f1 = range(19, 24)			#
f2 = range(0, 13)			#
luce = not(localtime()[3] in (f1 + f2))	#

#luce = GPIO.input(pinrele2)
venti = GPIO.input(pinventi)
# amaro tentativo
if t is not None and umi is not None:
	VPDUR = 100*(-0.9/(0.6108*math.exp(17.27*t/(t+237.3)))+1)
        VPDTEMP = (237.3*math.log((0.9)/(0.6108*(1-(umi/100))))/(17.27-math.log((0.9)/(0.6108*(1-(umi/100))))))
        VPD = 6.108*math.exp(17.27*t/(t+237.3))*(1-(umi/100))
	if VPD < 8  and umi > VPDUR:
		minimo = VPDTEMP - 1
		massimo = VPDTEMP - 0.5
		deltavg = (1.0, 1.2)
	elif VPD >= 8 and VPD < 8.2:
		print
	else:
	        minimo = 22
       		massimo = 22.4
        	deltavg = (1.3, 1.5)

else:
	minimo = 22
        massimo = 22.4
        deltavg = (1.3, 1.5)

print minimo, massimo

minN = 21
maxN = 21.5
deltav = (1.2, 1.3)

i = 0

while i < 4:
	if luce == 0 and luce is not None:	 
		if t < minimo and t is not None:
			GPIO.output(pinrele, GPIO.LOW)
			GPIO.output(pinventi, GPIO.LOW)
			print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Temperatura diurna bassa, stufa ON, luci='+repr(luce)+', ventilatore='+repr(venti))
			i = 4
		elif t > massimo and t is not None:
	                GPIO.output(pinrele, GPIO.HIGH)
                        if t > massimo + deltavg[1]:
				GPIO.output(pinventi, GPIO.LOW)
			elif t > massimo + deltavg[0]:
                                GPIO.output(pinventi, GPIO.LOW)
			elif t <= massimo + deltavg[0]:
	                        GPIO.output(pinventi, GPIO.HIGH)
			print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Temperatura diurna alta, stufa OFF, luci='+repr(luce)+', ventilatore='+repr(venti))
			i = 4
		elif t >= minimo and t <= massimo and t is not None:
#                        GPIO.output(pinventi, GPIO.LOW)
        	        print ('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Temperatura diurna OK, stufa OFF, luci='+repr(luce)+', ventilatore='+repr(venti))
			i = 4	
		elif t is None:
                        GPIO.output(pinventi, GPIO.HIGH)
		   	GPIO.output(pinrele, GPIO.HIGH)
           		print('Il sensore la ha scialata, None')
	                umi, t = Adafruit_DHT.read_retry(sensor, pinsensor, 5, 1)
                        i = i + 1
                        print i
		elif t < 11 and t > 50:
                        GPIO.output(pinventi, GPIO.HIGH)
			GPIO.output(pinrele, GPIO.HIGH)
			print('Il sensore ha dei problemi esce dal range 0-50C*')
        	        umi, t = Adafruit_DHT.read_retry(sensor, pinsensor)
			i = i + 1
			print i
		else:
     			print('Il sensore la ha scialata')
               		umi, t = Adafruit_DHT.read_retry(sensor, pinsensor, 5, 1)
			i = i + 1
	elif luce == 1 and luce is not None:
                if t < minN and t is not None:
                        GPIO.output(pinrele, GPIO.LOW)
                        GPIO.output(pinventi, GPIO.HIGH)
                        print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Temperatura notturna bassa, stufa ON, luci='+repr(luce)+', ventilatore='+repr(venti))
			i = 4
		elif t > maxN and t is not None:
			 GPIO.output(pinrele, GPIO.HIGH)
                         if t > maxN + deltav[1]:
                                GPIO.output(pinventi, GPIO.LOW)
                         elif t < maxN + deltav[0]:
			       GPIO.output(pinventi, GPIO.HIGH)
                         print('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                         print('Temperatura diurna alta, stufa OFF, luci='+repr(luce)+', ventilatore='+repr(venti))
               		 i = 4
		elif t >= minN and t <= maxN and t is not None:
                        GPIO.output(pinventi, GPIO.HIGH)
			print ('Temp={0:0.1f}*C Umidita={1:0.1f}%'.format(t, umi))
                        print('Temperatura diurna OK, stufa OFF, luci='+repr(luce)+', ventilatore='+repr(venti))                       
               		i = 4
		elif t is None:
                        GPIO.output(pinventi, GPIO.HIGH)
                        GPIO.output(pinrele, GPIO.HIGH)
                        print('Il sensore la ha scialata, None')
	                umi, t = Adafruit_DHT.read_retry(sensor, pinsensor, 5, 1)
                        i = i + 1
                        print i
		elif t < 0 and t > 50:
                        GPIO.output(pinventi, GPIO.HIGH)
                        GPIO.output(pinrele, GPIO.HIGH)
                        print('Il sensore ha dei problemi esce dal range 0-50C*')
	                umi, t = Adafruit_DHT.read_retry(sensor, pinsensor)
                        i = i + 1
                        print i

		else:
                        print('Il sensore la ha scialata')
	                umi, t = Adafruit_DHT.read_retry(sensor, pinsensor, 5, 1)
                        i = i + 1
                        print i
	else:
#		luce = GPIO.input(26)
		print ('localtime restituisce cazzate')


#except KeyboardInterrupt:
#	raise
#        print("Interrotto")
