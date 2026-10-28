"""CS 1001 - Lab Programming 2, Day 2
Lists and Strings Capstone

Complete the functions below using the design process discussed in class.
Each function must return a new list and must not modify its input list.
"""


def first_element(groups: list[list[int]]) -> list[int]:
    """Return the first element of each non-empty nested list."""
    result = []
    for group in groups:
        if len(group) > 0:
            result.append(group[0])
    return result


def long_words(words: list[str], minimum: int) -> list[str]:
    """Return strings whose length is greater than or equal to minimum."""
    result = []
    for word in words:
        if len(word) >= minimum:
            result.append(word)
    return result


def normalize_words(words: list[str]) -> list[str]:
    """Return non-empty strings converted to lowercase."""
    result = []
    for word in words:
        if word != "":
            result.append(word.lower())
    return result
