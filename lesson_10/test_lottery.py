import unittest
from lottery import generate_unique_random_numbers


class TestLottery(unittest.TestCase):

    def test_lottery_5_numbers(self):

        result = generate_unique_random_numbers(5)
        self.assertEqual(len(set(result)), 5)

    def test_lottery_50_numbers(self):

        result = generate_unique_random_numbers(50)
        self.assertEqual(len(set(result)), 50)

    def test_lottery_99_numbers(self):

        result = generate_unique_random_numbers(99)
        self.assertEqual(len(set(result)), 99)


if __name__ == '__main__':
    unittest.main(verbosity=2)
