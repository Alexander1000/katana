import socket
import yaml


class Server:
    listen: str
    port: int

    def __init__(self, config_file: str):
        self.__load_config(config_file)

    def __load_config(self, config_file: str) -> bool:
        file = open(config_file, "r")
        configs = yaml.load(file, Loader=yaml.FullLoader)
        file.close()

        assert 'server' in configs.keys(), "Expected field 'server' exists"
        srv_conf = configs.get('server')
        assert type(srv_conf).__name__ == 'dict', "Expected type 'dict' of 'server', but '%s' given" % type(srv_conf).__name__
        assert 'listen' in srv_conf.keys(), "Expected field 'listen' exists in 'server'"
        assert 'port' in srv_conf.keys(), "Expected field 'port' exists in 'server'"

        self.listen = srv_conf.get('listen')
        self.port = srv_conf.get('port')

        assert 'projectsDir' in configs.keys(), "Expected field 'projectsDir' exists"
        projects_dir = configs.get('projectsDir')
        assert type(projects_dir).__name__ == 'str'

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
