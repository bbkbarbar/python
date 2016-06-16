import socket
import sys
import argparse

debug_mode = False

parser = argparse.ArgumentParser('PWM commander client')
parser.add_argument("-c","--channel", type=str, help="output channel", default = 3)
parser.add_argument("-v","--value", type=str, help="pwm value (maybe in percentage)")
args = parser.parse_args()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 7967)
if debug_mode:
    print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    message = (args.value + " " + args.channel)
    if debug_mode:
        print >>sys.stderr, 'sending "%s"' % message
    if args.channel == "kill":
        sock.sendall("kill")
    else:
        sock.sendall(message)

    if args.channel != "kill":
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(32)
            amount_received += len(data)
            if debug_mode:
                print >>sys.stderr, 'received "%s"' % data

finally:
    #print >>sys.stderr, 'closing socket'
    sock.close()