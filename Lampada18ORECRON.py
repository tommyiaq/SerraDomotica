from time import localtime
from time import sleep
import  RPi.GPIO as  GPIO

GPIO.setmode(GPIO.BCM)

from time import localtime			#importo ogni volta per aggiornarla appena gli do hotspot con il telefono
acc1 = range(0,13)				#dalle 00.00.00 alle 12.59.59 
acc2 = range(19,25)				#dale 19.00.00 alle 23.59.59
if (localtime()[3] + 1) in (acc1 + acc2):	#ora da 0-24 + 1 per il fuso
	GPIO.setup(26, GPIO.OUT)
        GPIO.output(26, GPIO.LOW)
else:
  	GPIO.setup(26, GPIO.OUT)
        GPIO.output(26, GPIO.HIGH)
