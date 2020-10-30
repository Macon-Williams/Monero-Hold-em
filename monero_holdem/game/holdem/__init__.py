from monero_holdem.game.holdem.player import Player, PlayerPool
from monero_holdem.game.holdem.cards import Table, TableState
from monero_holdem.game.holdem.role import HoldemRole
from monero_holdem.game import Game
from deck_of_cards.deck_of_cards import DeckOfCards


class Holdem(Game):
    # Blind values in XMR
    SMALL_BLIND_VAL = 0.005
    BIG_BLIND_VAL = 0.01
    round_start = False

    def __init__(self):
        self.player_pool = PlayerPool()
        self.table = Table()
        self.table_state = TableState(table_state=TableState.PREFLOP)
        self.deck = DeckOfCards()
        super(Holdem, self).__init__()

    def add_user(self, user):
        # TODO? do stuff as the player joins
        self.player_pool.add_player(Player(user))

    def flop(self):
        self.deck.give_first_card()  # Burn a card
        for i in range(3):
            self.table.cards.append(self.deck.give_first_card())
        self.table_state = TableState.FLOP  # hmm

    def turn(self):
        self.deck.give_first_card()  # Burn a card
        self.table.cards.append(self.deck.give_first_card())
        self.table_state = TableState.TURN  # hmm

    def river(self):
        self.deck.give_first_card()  # Burn a card
        self.table.cards.append(self.deck.give_first_card())
        self.table_state = TableState.RIVER  # hmm

    # Assign roles (dealer, little blind, big blind) to the first 3 users in the room
    def assign_roles(self):
        self.player_pool.assign_roles()

    # Rotate the last user to the first user in the room
    def rotate_roles(self):
        self.player_pool.rotate_roles()

    # Forces small blind and big blind to put in money before cards are drawn
    def blind_bet(self):
        for pl in self.player_pool:
            if pl.role.role_type == HoldemRole.BIG_BLIND:
                self.table.add_pot(pl.bet_money(Holdem.BIG_BLIND_VAL))
            if pl.role.role_type == HoldemRole.SMALL_BLIND:
                self.table.add_pot(pl.bet_money(Holdem.SMALL_BLIND_VAL))

    def start_game(self):
        # do all the setup such as set dealers, etc
        self.assign_roles()
        self.blind_bet()
        self.round_start = True
        # ... TODO

        done = False
        while not done:
            for pl in self.player_pool:
                pl.take_turn()

        raise NotImplementedError
