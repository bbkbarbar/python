import subprocess
import socket
import argparse
import sys

#useage function
def useage():
	print
	print
	print "Example:"
	print "clientForTest.py -a 192.168.0.33 - 7629"
	exit(0)
#end useage function

#execute command funciton
def execute_command(cmd):
	cmd = cmd.rstrip()
	try: 
		results = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
	except Exception, e:
		results = "Could not execute the command: " + cmd

	return results
#end execute command funciton

def receive_data(client):
	try:
		while True:
			received_cmd = ""
			received_cmd += client.recv(8)

			if not received_cmd:
				continue

			cmd_results = execute_command(received_cmd)
			client.send(cmd_results)
	except Exception, e:
		print str(e)
		pass

def client_connect(host,port):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		client.connect((host,port))
		print "Connected to server: " + host + "@ port: " + str(port) 
		
		#receive_data(client)

		print "Enter a message to server: "
		input = sys.stdin.read()
		client.send(input)

	except Exception, e:
		print str(e)
		client.close()

def main():
	parser = argparse.ArgumentParser('Test client')
	parser.add_argument("-a","--address", type=str, help="The server IP address")
	parser.add_argument("-p","--port", type=int, help="The port number to connect with", default = 7629)

	args = parser.parse_args()

	if args.address == None:
		useage()

	target_host = args.address
	port_number = args.port

	client_connect(target_host,port_number)


if __name__ == "__main__":
	main()