import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Chips", 4, 1)

    def test_food_name(self):
        self.assertEqual("Chips", self.food.name)

    def test_food_price(self):
        self.assertEqual(4, self.food.price)

    def test_food_rejuvenation_level(self):
        self.assertEqual(1, self.food.rejuvenation_level)

