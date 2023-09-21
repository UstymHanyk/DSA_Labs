import unittest


def is_monotone(lst):
    increasing = decreasing = True

    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            decreasing = False
            break

    for i in range(0, len(lst) - 1):
        if lst[i] < lst[i + 1]:
            increasing = False
            break

    return increasing or decreasing


class TestIsMonotone(unittest.TestCase):

    def test_increasing(self):
        self.assertTrue(is_monotone([1, 2, 3, 4, 5]))

    def test_decreasing(self):
        self.assertTrue(is_monotone([5, 4, 3, 2, 1]))

    def test_non_monotone(self):
        self.assertFalse(is_monotone([1, 2, 2, 3, 2, 4]))


if __name__ == '__main__':
    unittest.main()
