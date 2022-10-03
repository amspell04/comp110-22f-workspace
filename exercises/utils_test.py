"""Test units for lists in utils.py"""


__author__: str = "730560818"


from exercises.utils import only_evans


def test_only_evans_empty() -> None:
    orig: list[int] = []
    assert only_evans(orig) == []


def test_only_evans_two_even_items() -> None:
    orig: list[int] = [2,4]
    assert only_evans(orig) == [2,4]


def test_only_evans_mixed_group() -> None:
    orig: list[int] = [2,3,4,5,6]
    assert only_evans(orig) == [2,4,6]


def test_only_evans_no_even() -> None:
    orig: list[int] = [1,5,3]
    assert only_evans(orig) == []


from exercises.utils import concat


def test_concat_empty_list_1() -> None:
    list_1: list[int] = []
    assert concat(list_1, [1,2]) == [1,2]


def test_concat_empty_list_2() -> None:
    list_2: list[int] = []
    assert concat([1,2], list_2) == [1,2]


def test_concat_large_sequence() -> None:
    list_1: list[int] = [1,2,3,4]
    list_2: list[int] = [5,6,7,8]
    assert concat(list_1, list_2) == [1,2,3,4,5,6,7,8]


def test_concat_negative_sequence() -> None:
    list_1: list[int] = [-1,-2,-3,-4]
    list_2: list[int] = [-5,-6,-7,-8]
    assert concat(list_1, list_2) == [-1,-2,-3,-4,-5,-6,-7,-8]


from exercises.utils import sub


def test_sub_empty() -> None:
    a_list: list[int] = []
    assert sub(a_list, 1, 3) == []


def test_sub_large_start() -> None:
    a_list: list[int] = [1,2,3]
    start: int = 5
    assert sub(a_list, start, 2) == []


def test_sub_small_end() -> None:
    a_list: list[int] = [1,2,3]
    end: int = -3
    assert sub(a_list, 2, end) == []


def test_sub_small_start() -> None:
    a_list: list[int] = [1,2,3]
    start: int = -3
    assert sub(a_list, start, 2) == [1,2]


def test_sub_large_end() -> None:
    a_list: list[int] = [1,2,3]
    end: int = 6
    assert sub(a_list, 1, end) == [2,3]


def test_sub_example_usage() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]