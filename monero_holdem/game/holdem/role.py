class RoleType(object):
    pass


class BigBlind(RoleType):
    pass


class SmallBlind(RoleType):
    pass


class Regular(RoleType):
    pass


class HoldemRole(object):
    BIG_BLIND = BigBlind()
    SMALL_BLIND = SmallBlind()
    REGULAR = Regular()

    def __init__(self, is_dealer, role_type):
        if not isinstance(role_type, RoleType):
            raise ValueError("Invalid role type, must be of type RoleType")

        self.is_dealer = is_dealer
        self.role_type = role_type
