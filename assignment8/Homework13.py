"""
Exercise-13: Rotate a list to the left by k positions
Write a function "rotate_left(my_list: list, k: int) -> list" that takes a
list of integers and an integer k, and returns a new list with the elements rotated k positions to the left.

Example:
rotate_left([1, 2, 3, 4, 5], 2) -> [3, 4, 5, 1, 2]
"""

def rotate_left(my_list: list, k: int) -> list:
    return my_list[k:] + my_list[:k]
print(rotate_left([1, 2, 3, 4, 5], 2))