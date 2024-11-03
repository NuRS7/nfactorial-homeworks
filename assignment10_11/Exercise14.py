"""
Exercise-14: Use reduce to Find the Maximum Number
Write a function "find_max(numbers: list) -> int" that uses reduce to find the maximum number in a list.

Example:
find_max([1, 2, 3, 4, 5]) -> 5
"""
from functools import reduce
def find_max(numbers: list) -> int:
    return reduce(max, numbers)
print(find_max([1, 2, 3, 4, 5,9,10,11,12,13,14,15,16,17,18,19,20]))