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
        for pl in self.players:
            pl.role.to_regular()
        self.players[-3].role.to_dealer()
        self.players[-2].role.to_small_blind()
        self.players[-1].role.to_big_blind()


class Player(object):
    def __init__(self, user):
        self.user = user
        self.cards = []
        self.amount_bet = 0.0
        self.fold = False
        self.ready = False
        self.all_in = False
        self.win = False
        self.role = HoldemRole(HoldemRole.REGULAR)

    def get_name(self):
        return self.user.name

    def player_draw(self, deck):
        self.cards.append(deck.give_first_card())

    def clear_cards(self, deck):
        for c in self.cards:
            deck.take_card(c.pop)

    def get_cards(self):
        return self.cards

    def get_balance(self):
        return self.user.xmr

    def add_balance(self, amount):
        self.user.xmr += amount

    def bet_money(self, amount):
        if amount > self.user.xmr:
            log(f"Error, {self.get_name()} tried to bet: {amount}. Not enough money available")
            return False
        else:
            self.user.xmr -= amount
            log(f"Subtracted {amount} from player: {self.get_name()}'s pool")
            self.amount_bet += amount
            return amount

    def get_round_bet(self):
        return self.amount_bet

    def call(self, current_bet):
        log(f"{self.get_name()} called.")
        self.bet_money(current_bet)

    def check(self):
        log(f"{self.get_name()} checked.")

    def fold(self):
        log(f"{self.get_name()} folded.")

    def raise_bet(self, amount):
        log(f"{self.get_name()} raised by {amount}")
        self.bet_money(amount)

    def take_turn(self, current_bet):
        # TODO make this sucker async babyyyyyy
        # if current_bet > self.get_round_bet():
            # Player can call or raise (if they have enough)... or they may fold
        # else:
            # Player can check, raise, or fold
        raise NotImplementedError
