"""
Exercise-2: Set Comprehension with Filtering
Write a function "unique_squares(numbers: List[int]) -> Set[int]" that uses a set comprehension to return the squares of the unique numbers from the input list.

Example:
unique_squares([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) -> {1, 4, 9, 16}
"""
from typing import List, Set


def unique_squares(numbers: List[int]) -> Set[int]:
    return {x**2 for x in set(numbers)}
print(unique_squares([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))