from monero_holdem.game.holdem.player import Player, PlayerPool
from monero_holdem.game.holdem.cards import Table
from monero_holdem.game.holdem.role import HoldemRole
from monero_holdem.game import Game
from deck_of_cards.deck_of_cards import DeckOfCards


class Holdem(Game):
    # Blind values in XMR
    SMALL_BLIND_VAL = 0.005
    BIG_BLIND_VAL = 0.01

    def __init__(self):
        self.player_pool = PlayerPool()
        self.table = Table()
        self.deck = DeckOfCards()
        super(Holdem, self).__init__()

    def add_user(self, user):
        # TODO? do stuff as the player joins
        self.player_pool.add_player(Player(user))

    def flop(self):
        self.deck.give_first_card()
        for i in range(3):
            self.table.cards.append(self.deck.give_first_card())
        self.table.flop = True

    def turn(self):
        # Burn a card
        self.deck.give_first_card()
        self.table.cards.append(self.deck.give_first_card())
        self.table.turn = True

    def river(self):
        # Burn a card
        self.deck.give_first_card()
        self.table.cards.append(self.deck.give_first_card())
        self.table.river = True

    # Assign roles (dealer, little blind, big blind)
    # Probably figure out how to make this better, 3 for loops is chonky.
    def assign_roles(self):
        self.player_pool.rotate_dealer()

    # Forces small blind and big blind to put in money before cards are drawn
    def blind_bet(self):
        for pl in self.player_pool:
            if pl.role.role_type == HoldemRole.BIG_BLIND:
                self.table.add_pot(pl.bet_money(Holdem.BIG_BLIND_VAL))
            if pl.role.role_type == HoldemRole.SMALL_BLIND:
                self.table.add_pot(pl.bet_money(Holdem.SMALL_BLIND_VAL))

        # TODO??

    def start_game(self):
        # do all the setup such as set dealers, etc
        # self.assign_roles()
        # self.blind_bet()
        # ... TODO

        done = False
        while not done:
            for pl in self.player_pool:
                pl.take_turn()

        raise NotImplementedError

# table = Table()
# deck = DeckOfCards()
# players = []
#
# # This is to test for now, the client will supply server with player information
# num_of_players = int(input("How many players? (1-9)"))
# for i in range(num_of_players):
#     name_of_player = input(f"Name {i + 1}?")
#     players.append(Player(name_of_player, 1, i))
#
# deck.shuffle_deck()
# assign_roles(players)
# flop(deck, table)
# time.sleep(1)
# turn(deck, table)
# time.sleep(1)
# river(deck, table)
