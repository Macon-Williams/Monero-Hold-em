from monero_holdem.log import log


class Deck(object):
    pass


class Table(object):
    def __init__(self):
        self.cards = []
        self.discard = []
        self.pot = 0.0
        self.state = TableState(TableState.PREFLOP)

    def list_cards(self):
        log("Cards currently on table:\n=-=-=-=-=-=-=-=-=-=-=-=-=")
        for i in range(len(self.cards)):
            log(self.cards[i].name)

    def add_card(self, card):
        self.cards.append(card)

    def discard_card(self, card):
        self.discard.append(card)

    def clear_cards(self, deck):
        for c in self.cards:
            self.discard.append(c.pop)
        for c in self.discard:
            deck.take_card(c.pop)

    def return_pot(self):
        return self.pot

    def clear_pot(self):
        self.pot = 0.0

    def add_pot(self, amount):
        self.pot += amount
        log(f"Added {amount} XMR to table pot.\nTotal XMR: {self.pot}")

    def reward_pot(self):
        award = self.pot
        self.pot = 0.0
        return award


class StateType(object):
    pass


class PreFlop(StateType):
    pass


class Flop(StateType):
    pass


class Turn(StateType):
    pass


class River(StateType):
    pass


class TableState(object):
    PREFLOP = PreFlop()
    FLOP = Flop()
    TURN = Turn()
    RIVER = River()

    def __init__(self, table_state):
        if not isinstance(table_state, StateType):
            raise ValueError("Invalid instance type, must be of type StateType")

        self.table_state = table_state

    def to_preflop(self):
        self.table_state = TableState.PREFLOP

    def to_flop(self):
        self.table_state = TableState.FLOP

    def to_turn(self):
        self.table_state = TableState.TURN

    def to_river(self):
        self.table_state = TableState.RIVER

