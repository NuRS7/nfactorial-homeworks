"""
Exercise-12: Set Comprehension to Intersect Sets
Write a function "intersection(sets: List[Set[Any]]) -> Set[Any]" that uses a set comprehension to return the intersection of a list of sets.

Example:
intersection([{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]) -> {3}
"""

from typing import List, Set, Any
def intersection(sets: List[Set[Any]]) -> Set[Any]:
    return {item for item in sets[0] if all(item in s for s in sets[1:])}
print(intersection([{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]))