import sqlite3
import datetime
import sys
import Adafruit_DHT
import time
from time import sleep

umid, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
unix = time.time()
data = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
conn = sqlite3.connect('prova1.db')
c = conn.cursor()
def log_values(date, temp, umid):
#	conn=sqlite3.connect('prova1.db')		     #It is important to provide an
							     #absolute path to the database
							     #file, otherwise Cron won't be
							     #able to find it!
#	c = conn.cursor()
#	umid, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
#	unix = time.time()
#       date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	c.execute('CREATE TABLE IF NOT EXISTS sensore(data TEXT, temp REAL, umid REAL)')
	c.execute("INSERT INTO sensore(data, temp, umid) VALUES(?, ?, ?)",
		(data, temp, umid))
        conn.commit()

def read_data():
        c.execute('SELECT * FROM sensore')
        #data = c.fetchall()
        #print(data)
        for row in c.fetchall():
                print(row)
	
#temperature = temperature * 9/5.0 + 32
# If you don't have a sensor but still wish to run this program, comment out all the 
# sensor related lines, and uncomment the following lines (these will produce random
# numbers for the temperature and humidity variables):
# import random
# humidity = random.randint(1,100)
# temperature = random.randint(10,30)

read_data()
while False:
	log_values(data, temp, umid)
	read_data()
	if umid is not None and temp is not None:
		log_values(data, temp, umid)	
	else:
		log_values(data, -999, -999)
	sleep(2)
conn.close()
