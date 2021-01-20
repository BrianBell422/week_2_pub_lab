class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def number_of_drinks(self):
        return len(self.drinks)

#Customer gives drink name
    def find_drink(self, drink_name_to_find):
        for drink in self.drinks:
            if drink.name == drink_name_to_find:
                return drink

#Pub checks customer can afford drink


#Pub removes money from cust wallet


#Pub adds money to till


#Pub gives drink to customer(customer, drink name)
    #If customer can buy drink
    #Drink bought = find_drink_by_name(drink name)
    #Customer decrease wallet(drink_bought.price)
    #Pub increase till (drink_bought.price)
    #Customer increase drunkenness (drink_bought.alcohol_level)

    


