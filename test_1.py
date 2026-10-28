import unittest

from day1 import increment_all, positive_values, lengths


class TestIncrementAll(unittest.TestCase):
    def test_single_value(self):
        self.assertEqual(increment_all([7]), [8])

    def test_returns_new_list(self):
        values = []
        self.assertIsNot(increment_all(values), values)

    def test_typical_values(self):
        self.assertEqual(increment_all([4, 9, 2, 1]), [5, 10, 3, 2])

    def test_empty_list(self):
        self.assertEqual(increment_all([]), [])

    def test_negative_zero_and_positive(self):
        self.assertEqual(increment_all([-2, 0, 3]), [-1, 1, 4])

    def test_input_is_not_modified(self):
        values = [4, 9, 2, 1]
        original = [4, 9, 2, 1]
        increment_all(values)
        self.assertEqual(values, original)


class TestPositiveValues(unittest.TestCase):
    def test_all_positive_values(self):
        values = [5, 2, 5]
        result = positive_values(values)
        self.assertEqual(result, [5, 2, 5])
        self.assertIsNot(result, values)

    def test_mixed_values(self):
        self.assertEqual(positive_values([-3, 5, 0, -1, 8, 2]), [5, 8, 2])

    def test_empty_list(self):
        self.assertEqual(positive_values([]), [])

    def test_no_positive_values(self):
        self.assertEqual(positive_values([-4, 0, -2]), [])

    def test_input_is_not_modified(self):
        values = [-3, 5, 0, -1, 8, 2]
        original = [-3, 5, 0, -1, 8, 2]
        positive_values(values)
        self.assertEqual(values, original)


class TestLengths(unittest.TestCase):
    def test_returns_new_list(self):
        words = []
        self.assertIsNot(lengths(words), words)

    def test_typical_strings(self):
        self.assertEqual(lengths(["cat", "computer", "", "hi"]), [3, 8, 0, 2])

    def test_empty_list(self):
        self.assertEqual(lengths([]), [])

    def test_single_string(self):
        self.assertEqual(lengths(["python"]), [6])

    def test_input_is_not_modified(self):
        words = ["cat", "computer", "", "hi"]
        original = ["cat", "computer", "", "hi"]
        lengths(words)
        self.assertEqual(words, original)


if __name__ == "__main__":
    unittest.main()
