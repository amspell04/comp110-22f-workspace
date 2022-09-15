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
       
def max(list:str) -> int:
    

