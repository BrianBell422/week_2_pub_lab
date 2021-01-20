import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        drinks = ["beer", "whiskey"]
        self.pub = Pub("The Prancing Pony", 100, drinks)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_cash(self):
        self.assertEqual(100, self.pub.cash)

    def test_pub_number_of_drinks(self):
        self.assertEqual(2, self.pub.number_of_drinks())

