"""List practice."""
__author__ = "730392807"


def all(int_list: list[int], integer: int) -> bool:
    """Seeing if all the integers in the list match the argument."""
    index = 0
    if len(int_list) == 0:
        return False
    while index < len(int_list):
        if integer != int_list[index]:
            return False
        index += 1
        
    return True


def max(highest: list[int]) -> int:
    """Choosing the highest value."""
    if len(highest) == 0:
        raise ValueError("max() arg is an empty List")
    tracker = 0
    value = highest[0]
    while tracker < len(highest):
        if value < highest[tracker]:
            value = highest[tracker]
        tracker += 1

    return value


def is_equal(list_a: list[int], list_b: list[int]) -> bool:
    """Seeing if the integers in each index correspond to each other in both lists."""
    turn = 0
    
    if len(list_a) == 0 or len(list_b) == 0:
        if len(list_a) == 0 and len(list_b) == 0:
            return True
        else:
            return False

    if len(list_a) != len(list_b):
        return False
    while turn < (len(list_a)) and turn < (len(list_b)):
        if list_a[turn] != list_b[turn]:
            return False
        turn += 1

    return True
            
