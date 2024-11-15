"""
Exercise-5: Nested List Comprehension to Compute Cartesian Product
Write a function "cartesian_product(set_a: List[Any], set_b: List[Any]) -> List[Tuple[Any, Any]]" that uses a nested list comprehension to compute the Cartesian product of two sets. The Cartesian product of two sets is the set of all ordered pairs (a, b) where a is in set_a and b is in set_b.

Example:
cartesian_product([1, 2], ['a', 'b']) -> [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
"""
from typing import List, Any, Tuple
def cartesian_product(set_a: List[Any], set_b: List[Any]) -> List[Tuple[Any, Any]]:
    return [(a, b) for a in set_a for b in set_b]
print(cartesian_product([1, 2], ['a', 'b']))