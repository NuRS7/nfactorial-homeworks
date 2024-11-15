"""
Exercise-18: Set Comprehension to Find Common Elements
Write a function "common_elements(lists: List[List[Any]]) -> Set[Any]" that uses a set comprehension to find the common elements in a list of lists.

Example:
common_elements([[1, 2, 3], [2, 3, 4], [3, 4, 5]]) -> {3}
"""
from typing import List, Any, Set
def common_elements(lists: List[List[Any]]) -> Set[Any]:
    return {x for x in set(lists[0]) if all(x in l for l in lists[1:])}
print(common_elements([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))