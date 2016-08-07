import subprocess
import os


def get_temperature():
    "Returns the temperature in degrees C"
    try:
        s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
        return float(s.split('=')[1][:-3])
    except:
        return 0

    

#print("\033[1;32;40m Bright Green  \n")
def showCPUTempWithColors():
	print 'Temperature: |' +str(get_temperature()) + "|'C"
	#print("\033[" + color + text)


showCPUTempWithColors()
