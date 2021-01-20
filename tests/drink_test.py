import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Beer", 5, 1)

    def test_drink_name(self):
        self.assertEqual = ("Beer", self.drink.name)

    def test_drink_price(self):
        self.assertEqual = (5, self.drink.price)

    def test_drink_alcohol_level(self):
        self.assertEqual = (1, self.drink.alcohol_level)

