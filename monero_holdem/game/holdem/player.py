from monero_holdem.log import log
from monero_holdem.game.holdem.role import HoldemRole


class PlayerPool(object):
    def __init__(self):
        self.players = []

    def __iter__(self):
        for p in self.players.keys():
            yield p

    def add_player(self, player):
        self.players[player.user.address] = player

    def get_player(self, address):
        return self.players[address]

    def get_player_count(self):
        return len(self.players)

    def rotate_roles(self):
        self.players = self.players[-1:] + self.players[:-1]

    # TODO: Is this the correct way to implement this? I feel like I'm reinitializing the objects
    # Assumes that we have at least 3 players on a table, 2 of which can be bots
    # Also, should dealer just be a standard role too instead of us keeping track with a boolean?
    def assign_roles(self):
        for i in range(3):
            if i == 0:
                self.players[i].role = HoldemRole(True, role_type=HoldemRole.REGULAR)
            if i == 1:
                self.players[i].role = HoldemRole(False, role_type=HoldemRole.SMALL_BLIND)
            if i == 2:
                self.players[i].role = HoldemRole(False, role_type=HoldemRole.BIG_BLIND)


class Player(object):
    def __init__(self, user):
        self.user = user
        self.cards = []
        self.fold = False
        self.ready = False
        self.all_in = False
        self.role = HoldemRole(False, role_type=HoldemRole.REGULAR)
        self.win = False
        self.balance = 0

    def take_turn(self):
        # TODO make me async
        print("What would you like to do?")
        # if ...
        raise NotImplementedError

    def __repr__(self):
        return self.user.name

    def player_draw(self, deck):
        self.cards.append(deck.give_first_card())

    def get_cards(self):
        return self.cards

    def get_balance(self):
        return self.balance

    def add_balance(self, amount):
        self.balance += amount

    def bet_money(self, amount):
        if amount > self.balance:
            log("Error, not enough money available")
            return False
        else:
            self.balance -= amount
            log("Subtracted " + str(amount) + " from player's pool")
            return amount
