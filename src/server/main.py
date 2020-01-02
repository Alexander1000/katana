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

    def __assert_key_exists(self, path: str, key: str, data: dict) -> bool:
        if key not in data.keys():
            if len(path) > 0:
                raise AssertionError("Expected field '%s' exists in path '%s'" % (key, path))
            else:
                raise AssertionError("Expected field '%s' exists" % key)
        return True

    def __assert_type(self, path: str, data_type: str, data) -> bool:
        if type(data).__name__ != data_type:
            raise AssertionError("Expected type '%s' of '%s', but '%s' given" % (data_type, path, type(data).__name__))
        return True

    def validate(self, configs: dict) -> bool:
        self.__assert_key_exists('', 'server', configs)
        srv_conf = configs.get('server')
        self.__assert_type('server', 'dict', srv_conf)
        self.__assert_key_exists('server', 'listen', srv_conf)
        self.__assert_key_exists('server', 'port', srv_conf)

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
