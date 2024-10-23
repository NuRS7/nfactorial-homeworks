"""
Exercise-14: Rotate a list to the right by k positions
Write a function "rotate_right(my_list: list, k: int) -> list" that
takes a list of integers and an integer k, and returns a new list
with the elements rotated k positions to the right.

Example:
rotate_right([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
"""

def rotate_right(my_list: list, k: int) -> list:
    return my_list[-k:] + my_list[:-k]
print(rotate_right([1, 2, 3, 4, 5], 2))
