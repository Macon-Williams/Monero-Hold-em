from monero_holdem.game.holdem.player import Player, PlayerPool
from monero_holdem.game.holdem.cards import Table, TableState
from monero_holdem.game.holdem.role import HoldemRole
from monero_holdem.log import log
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

    # TODO, ask about this
    def deal_player_cards(self):
        for i in range(2):
            for j in range(self.player_pool.get_player_count()):
                self.player_pool.get_player(j-2).player_draw(self.deck)  # Small blind is dealt a card first

    def flop(self):
        self.table.discard_card(self.deck.give_first_card())  # Burn a card
        for i in range(3):
            self.table.add_card(self.deck.give_first_card())
        self.table.state.to_flop()
        self.table.list_cards()

    def turn(self):
        self.table.discard_card(self.deck.give_first_card())  # Burn a card
        self.table.add_card(self.deck.give_first_card())
        self.table.state.to_turn()
        self.table.list_cards()

    def river(self):
        self.table.discard_card(self.deck.give_first_card())  # Burn a card
        self.table.add_card(self.deck.give_first_card())
        self.table.state.to_river()
        self.table.list_cards()

    # Assign roles (dealer, little blind, big blind) to the first 3 users in the room
    def assign_roles(self):
        self.player_pool.assign_roles()

    # Rotate the last user to the first user in the room
    def rotate_roles(self):
        self.player_pool.rotate_roles()

    # Forces small blind and big blind to put in money before cards are drawn
    def blind_bet(self):
        for p in self.player_pool:
            if p.role.role_type == HoldemRole.BIG_BLIND:
                self.table.add_pot(p.bet_money(Holdem.BIG_BLIND_VAL))
            if p.role.role_type == HoldemRole.SMALL_BLIND:
                self.table.add_pot(p.bet_money(Holdem.SMALL_BLIND_VAL))

    def bet_round(self, starting_bet):
        current_bet = starting_bet  # Keep track of the individual current bet
        for p in self.player_pool:
            log(f"{p.get_name()}"'s turn')
            p.take_turn(current_bet)

    def start_game(self):
        # do all the setup such as set dealers, etc
        table_active = True
        while table_active:
            self.assign_roles()
            self.blind_bet()
            self.deal_player_cards()

            log(f"Pre-flop begins.")
            # Start bet

            log(f"Flop begins.")
            self.flop()
            # Start bet

            log(f"Turn begins.")
            self.turn()
            # start bet

            log(f"River begins.")
            self.river()
            # Start bet

            # TODO Check cards
            # TODO Payout winner

            table_active = False

        # raise NotImplementedError
