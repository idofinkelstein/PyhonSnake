import unittest
from .food import Food


class TestFood(unittest.TestCase):

    def test_food_redraw(self):
        food = Food(600, 600)

