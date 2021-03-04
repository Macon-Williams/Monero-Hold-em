import socket


class Connection:
    def __init__(self, ip_address, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip_address = ip_address
        self.server_port = port
        self.address = (self.server_ip_address, self.server_port)
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            pass
