import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("beer", 5, 1)
        self.drink_2 = Drink("whiskey", 10, 3)
        drinks = [self.drink_1, self.drink_2]
        self.pub = Pub("The Prancing Pony", 100, drinks)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_number_of_drinks(self):
        self.assertEqual(2, self.pub.number_of_drinks())

    def test_find_drink(self):
        drink = self.pub.find_drink("beer")
        self.assertEqual(self.drink_1, drink)

    def test_can_customer_afford_item(self):
        customer = Customer("John", 20, 100, 0)
        self.assertEqual(True, self.pub.can_customer_afford_item(customer, self.drink_1))

    def test_add_money_to_till(self):
        self.pub.add_money_to_till(10)
        self.assertEqual(110, self.pub.till)

    def test_remove_money_from_till(self):
        self.pub.remove_money_from_till(10)
        self.assertEqual(90, self.pub.till)

    def test_check_age_pass(self):
        customer = Customer("John", 20, 100, 0)
        self.assertEqual(True, self.pub.check_age(customer))

    def test_check_age_fail(self):
        customer = Customer("John", 10, 100, 0)
        self.assertEqual(False, self.pub.check_age(customer))

    def test_sell_drink_to_customer_can_afford(self):
        customer = Customer("John", 20, 100, 0)
        self.pub.sell_drink_to_customer(customer, "beer")
        self.assertEqual(95, customer.wallet)
        self.assertEqual(105, self.pub.till)

    def test_sell_drink_to_customer_can_afford_too_young(self):
        customer = Customer("John", 10, 100, 0)
        self.pub.sell_drink_to_customer(customer, "beer")
        self.assertEqual(100, customer.wallet)
        self.assertEqual(100, self.pub.till)

    def test_sell_drink_to_customer_cannot_afford(self):
        customer = Customer("John", 20, 4, 0)
        self.pub.sell_drink_to_customer(customer, "beer")
        self.assertEqual(4, customer.wallet)
        self.assertEqual(100, self.pub.till)

    def test_increase_drunkenness(self):
        customer = Customer("John", 20, 100, 0)
        self.pub.sell_drink_to_customer(customer, "beer")
        self.assertEqual(1, customer.drunkenness)
