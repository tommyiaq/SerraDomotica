import sqlite3
import datetime
import sys
import Adafruit_DHT
import time
import RPi.GPIO as GPIO

conn = sqlite3.connect('STORICODHT22')
c = conn.cursor()

def log_values():
	gpiolist = [26, 19, 13, 6]
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(gpiolist, GPIO.OUT)
	rel1 = GPIO.input(26)
	rel2 = GPIO.input(19)
	rel3 = GPIO.input(13)
	rel4 = GPIO.input(6)
	
	umid, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
	unix = time.time()
	data = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

	c.execute('CREATE TABLE IF NOT EXISTS sensore(data TEXT, temp REAL, umid REAL, rel1 INT, rel2 INT, rel3 INT, rel4 INT)')
	c.execute("INSERT INTO sensore(data, temp, umid, rel1, rel2, rel3, rel4) VALUES(?, ?, ?, ?, ?, ?, ?)",
		(data, temp, umid, rel1, rel2, rel3, rel4))
        conn.commit()


def read_data():
        c.execute('SELECT * FROM sensore')
        for row in c.fetchall():
                print(row)

log_values()	
#read_data()
conn.close()
