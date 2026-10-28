import unittest

from day2 import first_element, long_words, normalize_words


class TestFirstElement(unittest.TestCase):
    def test_single_element_lists(self):
        self.assertEqual(first_element([[0], [-2], [5]]), [0, -2, 5])

    def test_returns_new_list(self):
        groups = []
        self.assertIsNot(first_element(groups), groups)

    def test_mixed_nested_lists(self):
        self.assertEqual(
            first_element([[1, 2, 3], [], [4, 5], [6], []]),
            [1, 4, 6],
        )

    def test_empty_outer_list(self):
        self.assertEqual(first_element([]), [])

    def test_all_nested_lists_empty(self):
        self.assertEqual(first_element([[], [], []]), [])

    def test_input_is_not_modified(self):
        groups = [[1, 2, 3], [], [4, 5], [6]]
        original = [[1, 2, 3], [], [4, 5], [6]]
        first_element(groups)
        self.assertEqual(groups, original)


class TestLongWords(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(long_words([], 3), [])

    def test_empty_string_is_too_short(self):
        self.assertEqual(long_words(["", "a"], 1), ["a"])

    def test_zero_minimum_includes_every_string(self):
        words = ["", "cat", "a", "cat"]
        result = long_words(words, 0)
        self.assertEqual(result, ["", "cat", "a", "cat"])
        self.assertIsNot(result, words)

    def test_negative_minimum(self):
        self.assertEqual(long_words(["", "hi"], -1), ["", "hi"])

    def test_typical_words(self):
        self.assertEqual(
            long_words(["cat", "elephant", "dog", "computer", "hi"], 4),
            ["elephant", "computer"],
        )

    def test_exact_minimum_length_is_included(self):
        self.assertEqual(long_words(["cat", "bird", "mouse"], 4), ["bird", "mouse"])

    def test_no_matching_words(self):
        self.assertEqual(long_words(["a", "to", "cat"], 5), [])

    def test_input_is_not_modified(self):
        words = ["cat", "elephant", "dog", "computer", "hi"]
        original = ["cat", "elephant", "dog", "computer", "hi"]
        long_words(words, 4)
        self.assertEqual(words, original)


class TestNormalizeWords(unittest.TestCase):
    def test_already_lowercase(self):
        words = ["hello", "world", "hello"]
        result = normalize_words(words)
        self.assertEqual(result, ["hello", "world", "hello"])
        self.assertIsNot(result, words)

    def test_mixed_case_and_spaces(self):
        self.assertEqual(normalize_words(["PyThOn", " ", "Hi!"]),
                         ["python", " ", "hi!"])

    def test_mixed_capitalization_and_empty_strings(self):
        self.assertEqual(
            normalize_words(["Hello", "", "WORLD", "Python", ""]),
            ["hello", "world", "python"],
        )

    def test_empty_list(self):
        self.assertEqual(normalize_words([]), [])

    def test_only_empty_strings(self):
        self.assertEqual(normalize_words(["", "", ""]), [])

    def test_input_is_not_modified(self):
        words = ["Hello", "", "WORLD", "Python", ""]
        original = ["Hello", "", "WORLD", "Python", ""]
        normalize_words(words)
        self.assertEqual(words, original)


if __name__ == "__main__":
    unittest.main()
