import unittest
from unittest.mock import patch
import pizza

class TestPizza(unittest.TestCase):
    def test_get_number_int(self):
        with patch('pizza.get_word', return_value='42'):
            self.assertEqual(pizza.get_number(), 42)

    def test_get_number_float(self):
        with patch('pizza.get_word', return_value='3.14'):
            self.assertEqual(pizza.get_number(), 3.14)

if __name__ == '__main__':
    unittest.main()
