"""Example implementing a list utility funciton."""
# function name is contains
# We will have two parameters: needles(str), haystack list([str])
# Return type bool 
# gameplan:
# 1. Start with the first index
# 2. Loop through every index. Test if every index equal to needle. If true return True! We found it! 
# 3. Return False


def contains(needles:str, haystack:(list[str])) -> bool:
    i: int = 0
    while i < len(haystack):
        if needles == haystack[i]:
            return True
        i += 1
    return False

