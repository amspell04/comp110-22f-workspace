"""An example defintion function. """

def my_max(a: int, b: int) -> int:
    """Returns the largest argument. """
    if a >= b:
        return a 
    else:
        return b
print(my_max(10 + 1, 10))
results: int = (my_max(15,100))
print(results)