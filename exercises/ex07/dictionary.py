"""Dictionary, exercise 7, work."""


__author__: str = "730560818"


def invert(orig: dict[str, str]) -> dict[str, str]:
    """This function returns the given dictionary in an inverted form. Switches keys for values and values for keys."""
    invert_orig: dict[str, str] = {}
    for key in orig:
        if orig[key] in invert_orig:
            """Key Error raises if two keys of the same name exist."""
            raise KeyError("Two keys are the same!")
        invert_orig[orig[key]] = key
    return invert_orig


def favorite_color(colors: dict[str, str]) -> str:
    """This function returns the most popular color of a given dicitonary."""
    counter: dict[str, int] = {}
    max: str = ""
    temp: int = 0
    for key in colors:
        color_present: bool = colors[key] in counter
        if color_present is True:
            counter[colors[key]] = (counter[colors[key]] + 1)       
        if color_present is False:
            counter[colors[key]] = 1
    for key in counter:
        if counter[key] > temp:
            temp = counter[key]
            max = key
    return max


def count(count_list: list[str]) -> dict[str, int]:
    """This function counts the existence of a str in a given list and displays these strings with their given count in a dictionary."""
    i: int = 0
    result: dict[str, int] = {}
    while i < len(count_list):
        is_i_present: bool = count_list[i] in result 
        print(is_i_present)
        if is_i_present is False:
            result[count_list[i]] = 1
        if is_i_present is True:
            result[count_list[i]] = (result[count_list[i]] + 1)
        i += 1
    return result