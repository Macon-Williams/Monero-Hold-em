class Deck(object):
    pass


class Table(object):
    def __init__(self):
        self.cards = []
        self.pot = 0.0

    def list_cards(self):
        for i in range(len(self.cards)):
            print(self.cards[i].name)

    def return_pot(self):
        return self.pot

    def add_pot(self, amount):
        self.pot += amount


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
