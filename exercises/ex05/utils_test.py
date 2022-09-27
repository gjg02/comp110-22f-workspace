"""EX05 - Docstring placeholder"""
__author__ = "730392807"


from utils import only_evens
#from utils import concat

def evens_list() -> None:
    int_list: list[float] = []
    assert only_evens(int_list) == ()


def concat() -> None:
    list_a: list[int] =[]
    list_b: list[int] = []
    return list_a + list_b