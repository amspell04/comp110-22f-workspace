"""This is the where the test functions for the dictioonary file exist."""


__author__: str = "730560818"


from dictionary import invert
import pytest
from dictionary import favorite_color
from dictionary import count


def test_invert_short_sequence() -> None:
    """This function tests the invert function using a short sequence."""
    orig: dict[str, str] = ({'a': 'z', 'b': 'y', 'c': 'x'})
    assert invert(orig) == ({'z': 'a', 'y': 'b', 'x': 'c'})


def test_invert_long_sequence() -> None:
    """This function tests the invert function using a longer sequence."""
    orig: dict[str, str] = ({'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h'})
    assert invert(orig) == ({'b': 'a', 'd': 'c', 'f': 'e', 'h': 'g'})


def test_key_error() -> None:
    """This function tests for the KeyError to be raised when two keys are the same."""
    with pytest.raises(KeyError):
        orig: dict[str, str] = ({'kris': 'jordan', 'micheal': 'jordan'})
        invert(orig)


def test_favorite_color_mix() -> None:
    """This function tests the favorite_color function using a short mixed list."""
    colors: dict[str, str] = ({'a': 'blue', 'b': 'red', 'c': 'red'})
    assert favorite_color(colors) == 'red'


def test_favorite_color_tied() -> None:
    """This function tests the favorite_color function when there is a tie between values."""
    colors: dict[str, str] = ({'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue'})
    assert favorite_color(colors) == 'red'


def test_favorite_color_same_value() -> None:
    """This function tests the favorite_color funciton when all the same values exist."""
    colors: dict[str, str] = ({'a': 'red', 'b': 'red'})
    assert favorite_color(colors) == 'red'


def test_count_mixed() -> None:
    """This tests the count function using a small list."""
    count_list: list[str] = (["a", "b", "a"])
    assert count(count_list) == ({'a': 2, 'b': 1})


def test_count_no_repeating() -> None:
    """This tests the count funciton using a list where all keys only have value of one."""
    count_list: list[str] = (["a", "b", "c"])
    assert count(count_list) == ({'a': 1, 'b': 1, 'c': 1})


def test_count_all_repeating() -> None:
    """This tests the count funciton when only one key exists."""
    count_list: list[str] = (["a", "a", "a"])
    assert count(count_list) == ({'a': 3})