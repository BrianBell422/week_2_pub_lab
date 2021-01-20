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

