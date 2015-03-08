import RPi.GPIO as GPIO
import json
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.output(23,1)
def get_pinstate():
	pins = [4,17,27,22,18,23,24,25]
	print pins
	pinstate = {}
	for i in pins:
		GPIO.setup(i,GPIO.OUT)
		if (GPIO.input(i)):		
			pinstate[str(i)] = "ON"
		else:
			pinstate[str(i)] = "OFF"

	#pinstate = json.dumps(pinstate)
	print pinstate


get_pinstate()