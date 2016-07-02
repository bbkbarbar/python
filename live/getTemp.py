# Temp.py

from ds18b20 import DS18B20   
import argparse

parser = argparse.ArgumentParser('Temperature reader')
parser.add_argument("-s","--sensorChannel", type=int, help="temperature sensor channel", default = 0)
args = parser.parse_args()
sensor = args.sensorChannel

# test temperature sensors
x = DS18B20()
count=x.device_count()

if sensor == -1:
	strResult = str(count) + " "
	i = 0
	while i < count:
	   strResult += ('%.3f' % x.tempC(i))
	   i += 1
	   if i < count:
	   		strResult += " "
	print(strResult)
else:
	if sensor < count:
		print('%.3f' % x.tempC(sensor))		

