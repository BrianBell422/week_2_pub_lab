class Customer:
    def __init__(self, name, age, wallet, drunkenness):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.drunkenness = drunkenness

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level

    def decrease_drunkenness(self, drink):
        self.drunkenness -= drink.alcohol_level

    def increase_wallet(self, money):
        self.wallet += money

    def decrease_wallet(self, money):
        self.wallet -= money

