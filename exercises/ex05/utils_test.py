"""Test units for lists in utils.py."""


__author__: str = "730560818"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """This tests the only_evens function when it is empty."""
    orig: list[int] = []
    assert only_evens(orig) == []


def test_only_evens_two_even_items() -> None:
    """This tests the only_evens function when two even items are present."""
    orig: list[int] = [2, 4]
    assert only_evens(orig) == [2, 4]


def test_only_evens_mixed_group() -> None:
    """This tests the only_evens function using a list of mixed even and odd integers."""
    orig: list[int] = [2, 3, 4, 5, 6]
    assert only_evens(orig) == [2, 4, 6]


def test_only_evens_no_even() -> None:
    """This tests the only_evens function using a list with only odds. The output from the function should be empty brackets."""
    orig: list[int] = [1, 5, 3]
    assert only_evens(orig) == []


def test_concat_empty_list_1() -> None:
    """This tests the concat function for an empty list. The output should be empty brackets."""
    list_1: list[int] = []
    assert concat(list_1, [1, 2]) == [1, 2]


def test_concat_empty_list_2() -> None:
    """This tests the concat function for an empty list. The expected output is empty brackets."""
    list_2: list[int] = []
    assert concat([1, 2], list_2) == [1, 2]


def test_concat_large_sequence() -> None:
    """This tests the concat function for a lrge sequence of integers in both list 1 and list 2."""
    list_1: list[int] = [1, 2, 3, 4]
    list_2: list[int] = [5, 6, 7, 8]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_negative_sequence() -> None:
    """This tests the concat function using a sequence of negative integers."""
    list_1: list[int] = [-1, -2, -3, -4]
    list_2: list[int] = [-5, -6, -7, -8]
    assert concat(list_1, list_2) == [-1, -2, -3, -4, -5, -6, -7, -8]


def test_sub_empty() -> None:
    """This tests the sub function for an empty list. The expected outcome is empty brackets."""
    a_list: list[int] = []
    assert sub(a_list, 1, 3) == []


def test_sub_large_start() -> None:
    """This tests the sub function for a start variable larger than the length of the given list. Expected output is an empty bracket."""
    a_list: list[int] = [1, 2, 3]
    start: int = 5
    assert sub(a_list, start, 2) == []


def test_sub_small_end() -> None:
    """This tests the sub function for an end variable which is smaller than 0. The output expected is empty brackets."""
    a_list: list[int] = [1, 2, 3]
    end: int = -3
    assert sub(a_list, 2, end) == []


def test_sub_small_start() -> None:
    """This tests the sub function with a start variable which is too small to be an indice. The start variable is set to 0."""
    a_list: list[int] = [1, 2, 3]
    start: int = -3
    assert sub(a_list, start, 2) == [1, 2]


def test_sub_large_end() -> None:
    """This tests the sub function for an end variable which is larger than the length of the list. The end variable is set to the last index of the list."""
    a_list: list[int] = [1, 2, 3]
    end: int = 6
    assert sub(a_list, 1, end) == [2, 3]


def test_sub_example_usage() -> None:
    """This tests the sub function for common usage which may appear, using the example from the instructions."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]