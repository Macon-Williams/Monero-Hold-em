class RoleType(object):
    pass


class Dealer(RoleType):
    pass


class BigBlind(RoleType):
    pass


class SmallBlind(RoleType):
    pass


class Regular(RoleType):
    pass


class HoldemRole(object):
    DEALER = Dealer()
    BIG_BLIND = BigBlind()
    SMALL_BLIND = SmallBlind()
    REGULAR = Regular()

    def __init__(self, role_type):
        if not isinstance(role_type, RoleType):
            raise ValueError("Invalid role type, must be of type RoleType")

        self.role_type = role_type

    def to_regular(self):
        self.role_type = HoldemRole.REGULAR

    def to_dealer(self):
        self.role_type = HoldemRole.DEALER

    def to_small_blind(self):
        self.role_type = HoldemRole.SMALL_BLIND

    def to_big_blind(self):
        self.role_type = HoldemRole.BIG_BLIND
