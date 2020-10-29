from monero_holdem.log import log
from monero_holdem.game.holdem.role import HoldemRole


class PlayerPool(object):
    def __init__(self):
        self.players = {
            # player_address: Player object
        }

    def __iter__(self):
        for p in self.players.keys():
            yield p

    def add_player(self, player):
        self.players[player.user.address] = player

    def get_player(self, address):
        return self.players[address]

    def rotate_dealer(self):
        # do the logic to move dealer, bb and sb
        #
        # role = ["deal", "bb", "sb"]
        # # Initialize the array according to the number of players
        # for i in range(len(player)):
        #     for j in range(len(player)):
        #         player[i].role.append("player")
        #
        # # Assign dealer, big blind, and small blind roles
        # for i in range(len(player)):
        #     for j in range(len(player)):
        #         if j < 3:
        #             player[i].role[j] = role[j]
        #
        # # Stagger the roles so that each round the blinds get shifted to a new player
        # for i in range(len(player)):
        #     player[i].role = (player[i].role[len(player[i].role) - i:len(player[i].role)] + player[i].role[
        #                                                                                     0:len(player[i].role) - i])

        raise NotImplementedError


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

    def player_draw(self, deck, player):
        for i in range(2):
            for j in player:
                player[j].cards.append(deck.give_first_card())

    def list_cards(self):
        log(self.user.name + "\n===================")
        for i in range(len(self.cards)):
            print(self.cards[i].name)

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

