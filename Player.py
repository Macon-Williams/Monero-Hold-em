class Player(object):
    def __init__(self, name, money, address):
        self.name = name
        self.money = money
        self.address = address
        self.cards = []
        self.fold = False
        self.ready = False
        self.all_in = False
        self.role = []
        self.win = False

    def __repr__(self):
        return self.name

    def list_cards(self):
        print(self.name + "\n===================")
        for i in range(len(self.cards)):
            print(self.cards[i].name)

    def get_money(self):
        return self.money
