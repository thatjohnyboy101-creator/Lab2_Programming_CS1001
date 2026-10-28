"""CS 1001 - Lab Programming 2, Day 1
Lists and Strings Capstone

Complete the functions below using the design process discussed in class.
Each function must return a new list and must not modify its input list.
"""


def increment_all(values: list[int]) -> list[int]:
    """Return a new list containing each value increased by 1."""
    result = []
    for value in values:
        result.append(value + 1)
    return result


def positive_values(values: list[int]) -> list[int]:
    """Return a new list containing only values strictly greater than 0."""
    result = []
    for value in values:
        if value > 0:
            result.append(value)
    return result


def lengths(words: list[str]) -> list[int]:
    """Return a new list containing the length of each string in words."""
    result = []
    for word in words:
        result.append(len(word))
    return result
