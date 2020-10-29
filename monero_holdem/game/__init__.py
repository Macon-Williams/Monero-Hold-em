from monero_holdem.game.holdem import Holdem


class Game(object):
    def __init__(self):
        pass

    def add_user(self, user):
        raise NotImplementedError

    def start_game(self):
        raise NotImplementedError
