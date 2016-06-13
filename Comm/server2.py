import socket
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Test server')
    parser.add_argument("-p","--port", type=int, help="The port number to connect with", default = 7629) #homepi mod 65535
    args = parser.parse_args()

    host = "localhost"
    port = args.port
    backlog = 5 
    size = 1024 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host,port)) 
    s.listen(backlog) 
    while 1: 
        client, address = s.accept() 
        data = client.recv(size) 
        if data: 
            client.send(data) 
        client.close()
     
