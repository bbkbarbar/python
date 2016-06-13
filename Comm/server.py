import socketserver
 
class Handler_TCPServer(socketserver.BaseRequestHandler):
    """
    The TCP Server class for demonstration.
 
    Note: We need to implement the Handle method to exchange data
    with TCP client.
 
    """
 
    def handle(self):
        # self.request -> TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} sent:".format(self.client_address[0]))
        print(self.data)
        # just send back ACK for data arrival confirmation
        self.request.sendall("ACK from TCP Server".encode())
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser('Test server')
    parser.add_argument("-p","--port", type=int, help="The port number to connect with", default = 7629) #homepi mod 65535
    args = parser.parse_args()

    HOST = "localhost"
    PORT = args.port
     
    # Init the TCP server object, bind it to the localhost on 9999 port
    tcp_server = socketserver.TCPServer((HOST, PORT), Handler_TCPServer)
 
    # Activate the TCP server.
    # To abort the TCP server, press Ctrl-C.
    tcp_server.serve_forever()