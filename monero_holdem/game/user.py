class User(object):
    def __init__(self, name, address, xmr):
        self.name = name
        self.address = address  # must be unique
        self.xmr = xmr


class Bot(User):
    def __init__(self, name):
        super(Bot, self).__init__(name, 0, 1)
