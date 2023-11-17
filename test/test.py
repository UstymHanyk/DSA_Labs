import unittest
from src.main import find_min_beer_coverage, read_input


class TestMinBeerTypes(unittest.TestCase):
    def test_scenario_1(self):
        input_filename = "input_1.txt"
        n, b, preferences = read_input(input_filename)
        result = find_min_beer_coverage(n, b, preferences)
        self.assertEqual(result, 2)

    def test_scenario_2(self):
        input_filename = "input_2.txt"
        n, b, preferences = read_input(input_filename)
        result = find_min_beer_coverage(n, b, preferences)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
