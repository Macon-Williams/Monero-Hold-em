class User(object):
    def __init__(self, name, address, xmr):
        self.name = name
        self.address = address
        self.xmr = xmr

    def update_name(self, name):
        self.name = name

    def update_address(self, address):
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address
