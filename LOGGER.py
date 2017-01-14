import sqlite3
import datetime
import sys
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
from time import sleep 
conn = sqlite3.connect('/home/pi/SerraDomotica/STORICODHT22')
c = conn.cursor()

gpiolist = [26, 19, 13, 6]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpiolist, GPIO.OUT)
def log_values():
	rel1 = GPIO.input(26)
	rel2 = GPIO.input(19)
	rel3 = GPIO.input(13)
	rel4 = GPIO.input(6)
	umid, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
	unix = time.time()
	data = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
#	umid = round(umid)
#	temp = round(temp)
	i = 0
        while i < 1:
#	        print (data, temp, umid, rel1, rel2, rel3, rel4)
		if temp is not None and umid is not None and umid < 100:
	        	umid = round(umid,1)
 			temp = round(temp,1)

#		while i < 1:		        	
			c.execute('CREATE TABLE IF NOT EXISTS sensore(data TEXT, temp REAL, umid REAL, rel1 INT, rel2 INT, rel3 INT, rel4 INT)')
			c.execute("INSERT INTO sensore(data, temp, umid, rel1, rel2, rel3, rel4) VALUES(?, ?, ?, ?, ?, ?, ?)",	 					
				(data, temp, umid, rel1, rel2, rel3, rel4))
        		conn.commit()
			i = i + 1
		else:
		        umid, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
	                if temp is not None and umid is not None and umid < 100:
	     			umid = round(umid,1)
        			temp = round(temp,1)
#			print('e che cazzo')
#        print (data, temp, umid, rel1, rel2, rel3, rel4)

log_values()

conn.close()
