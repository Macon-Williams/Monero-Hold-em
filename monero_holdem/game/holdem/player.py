from monero_holdem.log import log
from monero_holdem.game.holdem.role import HoldemRole


class PlayerPool(object):
    def __init__(self):
        self.players = []

    def __iter__(self):
        for p in self.players:
            yield p.user.address

    def add_player(self, player):
        self.players.append(player)

    def get_player_from_address(self, address):
        for pl in self.players:
            if pl.user.address == address:
                return pl
        raise ValueError("Player not found")

    def get_player(self, location):
        return self.players[location]

    def get_player_count(self):
        return len(self.players)

    def rotate_roles(self):
        self.players = self.players[-1:] + self.players[:-1]

    def assign_roles(self):
        self.players[0].role.to_dealer()
        self.players[1].role.to_small_blind()
        self.players[2].role.to_big_blind()


class Player(object):
    def __init__(self, user):
        self.user = user
        self.cards = []
        self.fold = False
        self.ready = False
        self.all_in = False
        self.role = HoldemRole(HoldemRole.REGULAR)
        self.balance = 0

    def take_turn(self):
        # TODO make me async
        print("What would you like to do?")
        # if ...
        raise NotImplementedError

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
            log(f"Error, {self.user.name} tried to bed: {amount}. Not enough money available")
            return False
        else:
            self.balance -= amount
            log(f"Subtracted {amount} from player: {self.user.name}'s pool")
            return amount
