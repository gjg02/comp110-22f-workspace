"""EX05 - Docstring placeholder."""
__author__ = "730392807"

def only_evens(int_list: list[int]) -> list[int]:
    """Return all even int."""
    index = 0
    value = ()
    while index < len(int_list):
        if int_list[index] % 2 == 0:
            value += int_list[index]
        index += 1

    return value


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """Return both lists of ints."""
    track_a = 0
    track_b = 0
    value_a = ()
    while track_a < len(list_a):
        value_a = list_a[track_a]
        track_a += 1

    value_b = ()
    while track_b < len(list_b):
        value_b = list_b[track_b]
        track_b += 1

    return value_a + value_b


#def sub(list_a: list[int], ) -> list:
