import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        drink_1 = Drink("beer", 5, 1)
        drink_2 = Drink("whiskey", 10, 3)
        drinks = [drink_1, drink_2]
        self.pub = Pub("The Prancing Pony", 100, drinks)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_number_of_drinks(self):
        self.assertEqual(2, self.pub.number_of_drinks())

    def test_find_drink(self, drink_name):
        self.pub.find_drink("beer")
        self.assertEqual(drink_1, drink_1)

