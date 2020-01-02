import socket
import yaml


class Server:
    def __init__(self, config_file: str):
        print("config %s" % config_file)
        file = open(config_file, "r")
        configs = yaml.load(file, Loader=yaml.FullLoader)
        file.close()
        print(configs)

    def init(self):
        # create tcp/ip socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket to the port
        server_address = ('127.0.0.1', 23866)
        print('starting up on %s port %s' % server_address)
        sock.bind(server_address)

        # Listen for incoming connections
        sock.listen(1)

        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = sock.accept()

            try:
                print('connection from', client_address)

                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(16)
                    print('received "%s"' % data)
                    if data:
                        print('sending data back to the client')
                        connection.sendall(data)
                    else:
                        print('no more data from', client_address)
                        break

            finally:
                # Clean up the connection
                connection.close()
