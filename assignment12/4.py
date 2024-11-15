"""
Exercise-4: Nested List Comprehension
Write a function "flatten(nested_list: List[List[Any]]) -> List[Any]" that uses a nested list comprehension to flatten a list of lists.

Example:
flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
from typing import List, Any


def flatten(nested_list: List[List[Any]]) -> List[Any]:
    return [i for j in nested_list for i in j]
print(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))