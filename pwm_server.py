import socket
import sys
import RPi.GPIO as GPIO

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
channel = 3
GPIO.setup(channel, GPIO.OUT)
p = GPIO.PWM(channel, 50)
pwmIsRunning = False
serverIsRunning = True

def setPwm(line):
	if pwmIsRunning == True:
		pwmIsRunning = False
		p.stop()

	if line == "stop":
		pwmIsRunning = False
		p.stop()
	else:		
		dc = float(line[:3])
		p.start(dc)
		pwmIsRunning = True



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
					p.stop()
					GPIO.cleanup()
					pwmIsRunning = False
					serverIsRunning = False
				else:
                	#print >>sys.stderr, 'sending data back to the client'
                	connection.sendall(data)
                	setPwm(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()