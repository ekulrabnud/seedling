import os
import glob
import time
import sqlite3

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
plant1 = glob.glob(base_dir + '28*')[1]
plant2 = glob.glob(base_dir + '28*')[0]
plants = [plant1,plant2]

device_files = [i + '/w1_slave' for i in plants] 


def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():

   
    
    lines = read_temp_raw(device_file)
    print lines

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(1)
        lines = read_temp_raw()
        print lines
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return round(temp_f,2)



def main():
    while True:
        conn = sqlite3.connect('tempdb.db')
        c = conn.cursor()
        print "reading temp"

        temps = [read_temp(i) for i in device_files]
        print temps
        c.execute(''' INSERT into plant1(temp,time)
                        VALUES (?,datetime())''',(temps[0],))
        c.execute(''' INSERT into plant2(temp,time)
                        VALUES (?,datetime())''',(temps[1],))
        conn.commit()
        conn.close()
        time.sleep(10)

if __name__ == '__main__':
    main()





	

