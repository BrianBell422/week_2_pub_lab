import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", 100, 0)

    def test_customer_name(self):
        self.assertEqual = ("John", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual = (100, self.customer.wallet)

    def test_increase_drunkenness(self):
        drink = Drink("beer", 5, 1)
        self.customer.increase_drunkenness(drink)
        self.assertEqual = (1, self.customer.drunkenness)

    def test_decrease_drunkenness(self):
        drink = Drink("beer", 5, 1)
        self.customer.decrease_drunkenness(drink)
        self.assertEqual = (-1, self.customer.drunkenness)

    def test_increase_wallet(self):
        money = 10
        self.customer.increase_wallet(money)
        self.assertEqual = (110, self.customer.wallet)

    def test_decrease_wallet(self):
        money = 10
        self.customer.decrease_wallet(money)
        self.assertEqual = (90, self.customer.wallet)

