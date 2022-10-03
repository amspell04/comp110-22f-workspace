"""Continueing to work with lists."""


__author__: str = "730560818"


def only_evens(orig: list[int]) -> list[int]:
    """This function looks into a list, finds the even integers, and returns only the even integers from the list."""
    i: int = 0
    new: list[int] = list()
    if len(orig) == 0:
        return []
    while i < len(orig):
        if (orig[i] % 2) == 0:
            new.append(orig[i])
        i += 1
    return new


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """This function combines the two lists given and lists their integers one after another."""
    combined: list[int] = list()
    i: int = 0
    while len(combined) < len(list_1):
        combined.append(list_1[i])
        i += 1
    i = 0
    while len(combined) < len(list_1) + len(list_2):
        combined.append(list_2[i])
        i += 1
    return combined


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """This list looks into a given list string and returns the start or end integers."""
    sub_list: list[int] = list()
    end -= 1
    if len(a_list) == 0 or start >= len(a_list) or end <= 0: 
        return []
    while len(sub_list) < 2:
        if start < 0: 
            start = 0
        if end > len(a_list):
            end = len(a_list) - 1
        sub_list.append(a_list[start])
        sub_list.append(a_list[end])
    return sub_list