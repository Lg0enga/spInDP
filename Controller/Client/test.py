import Adafruit_ADS1x15

import socket
import time
adc = Adafruit_ADS1x15.ADS1115()
#adc = Adafruit_ADS1x15.ADS1015()
#clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#clientsocket.connect(('10.42.0.76', 8000))


GAIN = 2/3
while True:
	spam = int(0.077 * adc.read_adc(0, gain=GAIN) - 1009.9), int(0.0771 * adc.read_adc(1, gain=GAIN) - 1016), int(adc.read_adc(2, gain=GAIN))

	#clientsocket.send(str(spam))
	print spam

	time.sleep(1)
