import sys
import socket
import argparse
import threading


# Test server

## global variables
clients = {}

def handleReceivedData(receivedData, client):
	print received_data

def client_serve(client):
	try:
		#print "Enter a command to execute on client: "
		#input = sys.stdin.read()
		#client.send(input)

		while True:
			#wait for data from listener
			received_data = client.recv(4096)
			handleReceivedData(received_data, client)

			##wait for more input
			#input = raw_input("")
			#input += "\n"

			#client.send(input)
	except:
		print "Client closed connection"
		pass


def server_listen(port_number):
	tartget_host = "0.0.0.0"
	listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listener.bind((tartget_host,port_number))
	listener.listen(25)

	print "Server is listening on port: " + str(port_number) + "..."

	while True:
		client,addr = listener.accept()
		print "Incomint connection accepted"
		clients[addr[0]] = client
		client_serve_thread = threading.Thread(target=client_serve, args=(client,))
		client_serve_thread.start()


def main():
	parser = argparse.ArgumentParser('Test server')                                                 
	parser.add_argument("-p","--port", type=int, help="The port number to connect with", default = 7629) #homepi mod 65535

	args = parser.parse_args()

	port_number = args.port

	server_listen(port_number)



if __name__ == "__main__":
	main()