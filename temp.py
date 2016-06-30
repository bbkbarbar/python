import os
import glob
import time
import datetime

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		temp_f = temp_c * 9.0 / 5.0 + 32.0
		return temp_c
		#, temp_f

def write_to_file(data):
	with open("temp.log", "a") as myfile:
		myfile.write(data + "\r\n")
		myfile.close()

while True:
	print(str(read_temp()) + "C")
	time = datetime.datetime.time(datetime.datetime.now())
	print(str(time)[:8])
	write_to_file(str(time)[:8] + "\t" + str(read_temp()))
	time.time.sleep(1)
