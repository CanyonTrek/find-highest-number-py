import unittest
from highest_number_finder import HighestNumberFinder

class TestHighestNumberFinder(unittest.TestCase):

    def test_highest_in_typical_list(self):
        finder = HighestNumberFinder()
        result = finder.find_highest_number([5, 9, 2])
        self.assertEqual(result, 9)

    def test_highest_with_negative_numbers(self):
        finder = HighestNumberFinder()
        result = finder.find_highest_number([-5, -1, -9])
        self.assertEqual(result, -1)

    def test_highest_with_empty_list_returns_none(self):
        finder = HighestNumberFinder()
        result = finder.find_highest_number([])
        self.assertIsNone(result)

    def test_highest_with_mixed_types(self):
        finder = HighestNumberFinder()
        result = finder.find_highest_number([3, 'a', 5.5, 2])
        self.assertEqual(result, 5.5)

if __name__ == "__main__":
    unittest.main()
