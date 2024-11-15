"""
Exercise-8: Nested Set Comprehension
Write a function "unique_values(nested_list: List[List[Any]]) -> Set[Any]" that uses a nested set comprehension to find the unique values in a nested list.

Example:
unique_values([[1, 2, 3], [2, 3, 4], [3, 4, 5]]) -> {1, 2, 3, 4, 5}
"""
from typing import List, Any, Set


def unique_values(nested_list: List[List[Any]]) -> Set[Any]:
    return {i for j in nested_list for i in j}
print(unique_values([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))