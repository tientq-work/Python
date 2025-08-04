import unittest
from utils import add, divide, greet

class TestUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_greet(self):
        self.assertEqual(greet("Thuận"), "Hello, Thuận!")

if __name__ == "__main__":
    unittest.main()
