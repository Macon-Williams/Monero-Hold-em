class User(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address  # must be unique


class Bot(User):
    def __init__(self, name):
        super(Bot, self).__init__(name, 0)
