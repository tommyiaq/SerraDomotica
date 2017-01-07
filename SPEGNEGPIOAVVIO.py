import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pinList = [ 17, 27, 22, 5, 6, 13, 19, 26]
i = 0 
while i < 8:
	GPIO.setup(pinList[i], GPIO.OUT)
	i = i + 1
GPIO.cleanup()
