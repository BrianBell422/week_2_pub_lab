class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def number_of_drinks(self):
        return len(self.drinks)

    def find_drink(self, drink_name_to_find):
        for drink in self.drinks:
            if drink.name == drink_name_to_find:
                return drink

    def can_customer_afford_item(self, customer, item):
        if customer.wallet >= item.price:
            return True
        else: return False

    def add_money_to_till(self, money):
        self.till += money

    def remove_money_from_till(self, money):
        self.till -= money

    def sell_drink_to_customer(self, customer, drink_name):
        drink = self.find_drink(drink_name)
        if self.can_customer_afford_item(customer, drink):
            customer.decrease_wallet(drink.price)
            self.add_money_to_till(drink.price)




#Pub gives drink to customer(customer, drink name)
    #If customer can buy drink
    #Drink bought = find_drink_by_name(drink name)
    #Customer decrease wallet(drink_bought.price)
    #Pub increase till (drink_bought.price)
    #Customer increase drunkenness (drink_bought.alcohol_level)

    


