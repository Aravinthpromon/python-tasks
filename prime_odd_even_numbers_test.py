import unittest
from prime_odd_even_numbers import categorize_numbers, is_prime

class TestCategorizeNumbers(unittest.TestCase):

    def test_categorize_numbers(self):
        start_range = 1
        end_range = 10
        result = categorize_numbers(start_range, end_range)

        expected_even = [2, 4, 6, 8, 10]
        expected_odd = [1, 3, 5, 7, 9]
        expected_prime = [2, 3, 5, 7]

        self.assertEqual(result["Even"], expected_even, "Even numbers mismatch.")
        self.assertEqual(result["Odd"], expected_odd, "Odd numbers mismatch.")
        self.assertEqual(result["Prime"], expected_prime, "Prime numbers mismatch.")

    def test_is_prime(self):
        self.assertTrue(is_prime(2), "2 should be prime.")
        self.assertTrue(is_prime(3), "3 should be prime.")
        self.assertFalse(is_prime(4), "4 should not be prime.")
        self.assertTrue(is_prime(5), "5 should be prime.")
        self.assertFalse(is_prime(1), "1 should not be prime.")
        self.assertFalse(is_prime(0), "0 should not be prime.")

if __name__ == "__main__":
    unittest.main()
