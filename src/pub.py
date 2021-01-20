class Pub:
    def __init__(self, name, cash, drinks):
        self.name = name
        self.cash = cash
        self.drinks = drinks

    def number_of_drinks(self):
        return len(self.drinks)

