"""Creating 3 functions!"""

__author__ = "730560818"


def all(list: list[int], single: int) -> bool:
    """This function determines whether the intergers in a list are equal to the singular given int."""
    i: int = 0
    if len(list) == 0:
        return False
    while i < len(list):
        if list[i] != single:
            return False
        if list[i] == single:
            i += 1
    return True
       

def max(input: list[int]) -> int:
    """This function tests each index of a list and returns the largest int."""
    idx: int = 0
    alt: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    while idx < len(input):
        if input[idx] > input[alt]:
            max = input[idx]
            alt += 1
        else:
            if input[alt] > input[idx]:
                max = input[alt]
        idx += 1
    return max


def is_equal(list_1: str, list_2: str) -> bool:
    """This function determines whether list_1 is completely equal list_2 based on their indices."""
    a: int = 0
    b: int = 0
    if list_1[a] == list_2[b]:
        a += 1
        b += 1
    if list_1[a] != list_2[b]:
        return False
    return True
