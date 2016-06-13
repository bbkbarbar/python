import socket
import argparse

parser = argparse.ArgumentParser('Test server')
parser.add_argument("-p","--port", type=int, help="The port number to connect with", default = 7629) #homepi mod 65535
parser.add_argument("-a","--addr", type=str, help="Server address", default = "192.168.0.101")
args = parser.parse_args()
 
host = args.addr
port = args.port
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port)) 
s.send('Hello, world') 
data = s.recv(size) 
s.close() 
print 'Received:', data