"""
Exercise-3: Nested Dictionary Comprehension
Write a function "dict_table(n: int) -> Dict[int, Dict[int, int]]" that creates a multiplication table in dictionary form.
The keys of the outer dictionary are numbers from 1 to 'n'. The values are inner dictionaries.
In the inner dictionary, the keys are numbers from 1 to 'n' and the values are the products of the outer and inner keys.

Example:
dict_table(3) -> {1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}
"""
from typing import Dict
def dict_table(n: int) -> Dict[int, Dict[int, int]]:
    return {i: {j: i * j for j in range(1, n + 1)} for i in range(1, n + 1)}
print(dict_table(3))
