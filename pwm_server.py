import socket
import sys
import RPi.GPIO as GPIO

# pwm1 -> ch3
# pwm2 -> ch5
# pwm3 -> ch7

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 7967)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Pwm init
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
freq = 50
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
p1 = GPIO.PWM(3, freq)
p2 = GPIO.PWM(5, freq)
p3 = GPIO.PWM(7, freq)
pwmIsRunning = False
serverIsRunning = True

def setPwm(line, running):
	res = False
	ch = str(line[4:2])
	print "ch: |" + ch + "|"
	if running == True:
		res = False
		p1.stop()

	if line == "stop":
		res = False
		p1.stop()
	else:		
		dc = float(line[:3])
		p1.start(dc)
		res = True
	return res



while serverIsRunning == True:
	# Wait for a connection
	print >>sys.stderr, 'waiting for a connection'
	connection, client_address = sock.accept()
	try:
		print >>sys.stderr, 'connection from', client_address

		# Receive the data in small chunks and retransmit it
		while True:
			data = connection.recv(32)
			#print >>sys.stderr, 'received "%s"' % data
			if data:
				if data == "kill":
					p1.stop()
					p2.stop()
					p3.stop()
					GPIO.cleanup()
					pwmIsRunning = False
					serverIsRunning = False
				else:
					#print >>sys.stderr, 'sending data back to the client'
					connection.sendall(data)
					pwmIsRunning = setPwm(data, pwmIsRunning)
			else:
				#print >>sys.stderr, 'no more data from', client_address
				break
			
	finally:
		# Clean up the connection
		connection.close()