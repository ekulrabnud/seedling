import os
import glob


os.system('sudo modprobe w1-gpio')
os.system('sudo modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
sensors = glob.glob(base_dir + '28*')

class Sensor():

    def __init__(self,id):
        self.id = id
        self.file = self.id + '/w1_slave'
        

    def read(self):
        f = open(self.file, 'rb')
        data = f.readlines()
        f.close()
    
        if data[0].strip()[-3:] == 'YES':
           
            equals_pos = data[1].find('t=')
         
            if equals_pos:
                temp_string = data[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                temp_f = temp_c * 9.0 / 5.0 + 32.0
                return round(temp_f,2)
   
    def log(self):
        pass

def main():
    sensors = [Sensor(i) for i in sensors]
    for i in sensors:
        print i.read()


if __name__ == '__main__':
    main()
