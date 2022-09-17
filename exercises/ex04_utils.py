"""Doct string here :)"""

__author__ = "730560818"

def all(list:str, single:int) -> bool:
    all = True
    i: int = 0
    while i < len(list):
        if list[i] != single:
            all = False
            return all
        if list[i] == single:
            i += 1
    return all
       
def max(input: list[int]) -> int:
    idx: int = 0
    alt: int = 1
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

def is_equal(list_1:str, list_2:str) -> bool:
    if list_1 == list_2:
        return True
    if list_1 != list_2:
        return False
