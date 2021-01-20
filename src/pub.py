class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def number_of_drinks(self):
        return len(self.drinks)

#Customer gives drink name
    def find_drink(self, drink_name):
        for drink in self.drinks:
            if self.drinks.name == drink_name:
                return drink

#Pub gets drink price

#Pub checks customer can afford drink

#Pub removes money from cust wallet

#Pub adds money to till


