import socket

parser = argparse.ArgumentParser('Test server')
parser.add_argument("-p","--port", type=int, help="The port number to connect with", default = 7629) #homepi mod 65535
parser.add_argument("-a","--addr", type=str, help="Server address", default = "192.168.0.101")
args = parser.parse_args()
 
host_ip, server_port = args.addr, args.port
data = " Hello how are you?\n"
 
# Initialize a TCP client socket using SOCK_STREAM
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
try:
    # Establish connection to TCP server and exchange data
    tcp_client.connect((host_ip, server_port))
    tcp_client.sendall(data.encode())
 
    # Read data from the TCP server and close the connection
    received = tcp_client.recv(1024)
finally:
    tcp_client.close()
 
print ("Bytes Sent:     {}".format(data))
print ("Bytes Received: {}".format(received.decode()))