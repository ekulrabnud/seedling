import sqlite3
import sensors
import time

sensors = [sensors.Sensor(i) for i in sensors.sensors]

conn = sqlite3.connect('tempdb.db')
c = conn.cursor()

def main():

	while True:
		temps = [i.read() for i in sensors]

		c.execute('''INSERT INTO soil(temp,time)
				VALUES(?,datetime())''',(temps[0],))
		c.execute('''INSERT INTO air(temp,time)
				VALUES(?,datetime())''',(temps[1],))
		conn.commit()
		print "%f and %f stored in db" %(temps[0],temps[1])
		time.sleep(900)

main()