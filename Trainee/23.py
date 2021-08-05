"""This is a testing module"""

from app import swap, average
import pytest


@pytest.mark.parametrize("test_arg, expected", [
    ("", ""),
    ("a", "a"),
    ("b", "b"),
    ("C", "C"),
    ("abc", "bca"),
    ("cab ", "b ca"),
    ("__test__", "st____te"),
    ("Hello, world!", " world!Hello,")
])
def test_swap(test_arg, expected):
    assert swap(test_arg) == expected


@pytest.mark.parametrize("test_arg, expected", [
    ([], 0),
    ([2], 2),
    ([-10], -10),
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 2.5),
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5, 6], 3.5),
    ([1, -1, 1, -1, 1, -1], 0),
    ([1, 2, 3, -10], -1)
])
def test_average(test_arg, expected):
    assert average(*test_arg) == expected
