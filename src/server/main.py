import socket
import yaml


class Server:
    listen: str
    port: int

    def __init__(self, config_file: str):
        file = open(config_file, "r")
        configs = yaml.load(file, Loader=yaml.FullLoader)
        file.close()

        self.validate(configs)

        server_config = configs.get('server')

        self.listen = server_config.get('listen')
        self.port = server_config.get('port')

    def validate(self, configs: dict) -> bool:
        if 'server' in configs.keys():
            srv_conf = configs.get('server')
            if type(srv_conf).__name__ != 'dict':
                raise AssertionError("Expected type dict, '%s' given" % type(srv_conf).__name__)
            if 'listen' not in srv_conf.keys():
                return False
            if 'port' not in srv_conf.keys():
                return False
        else:
            return False

        return True

    def init(self):
        # create tcp/ip socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket to the port
        server_address = (self.listen, self.port)
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
