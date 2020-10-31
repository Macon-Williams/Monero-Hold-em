from monero_holdem.log import log
from monero_holdem.game.holdem.role import HoldemRole


class PlayerPool(object):
    def __init__(self):
        self.players = []

    def __iter__(self):
        for p in self.players:
            yield p

    def add_player(self, player):
        self.players.append(player)

    def get_player_from_address(self, address):
        for p in self.players:
            if p.user.address == address:
                return p
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
        self.lobby = True
        self.role = HoldemRole(HoldemRole.REGULAR)

    def take_turn(self):
        # TODO make me async
        print("What would you like to do?")
        # if ...
        raise NotImplementedError

    def get_name(self):
        return self.user.name

    def player_draw(self, deck):
        self.cards.append(deck.give_first_card())

    # TODO make this better.
    # Can we discard the cards without manually clearing the cards array?
    def clear_cards(self):
        self.cards = []

    def get_cards(self):
        return self.cards

    def get_balance(self):
        return self.user.xmr

    def add_balance(self, amount):
        self.user.xmr += amount

    def bet_money(self, amount):
        if amount > self.user.xmr:
            log(f"Error, {self.user.name} tried to bed: {amount}. Not enough money available")
            return False
        else:
            self.user.xmr -= amount
            log(f"Subtracted {amount} from player: {self.user.name}'s pool")
            return amount
