from user import User


def log(val):
    print(val)


class Client(object):
    def __init__(self, name, address):
        user = User(name, address)


