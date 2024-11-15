"""
Exercise-2: List Comprehension with Nested Loop and Condition
Write a function "triple_combinations(lst: List[int]) -> List[Tuple[int, int, int]]" that returns all unique triple combinations (i, j, k)
from the given list that satisfy the condition i < j < k. Use a list comprehension with multiple 'for' clauses and a condition.

Example:
triple_combinations([1, 2, 3, 4]) -> [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
"""
from typing import List, Tuple
def triple_combinations(lst: List[int]) -> List[Tuple[int, int, int]]:
    return [(i, j, k) for i in lst for j in lst for k in lst if i < j < k]
print(triple_combinations([1, 2, 3, 4]))