"""
Exercise-14: Dictionary Comprehension to Map Strings to Lengths
Write a function "str_lengths(strings: List[str]) -> Dict[str, int]" that uses a dictionary comprehension to map strings to their lengths.

Example:
str_lengths(['hello', 'world', 'python']) -> {'hello': 5, 'world': 5, 'python': 6}
"""
from typing import Dict, List
def str_lengths(strings: List[str]) -> Dict[str, int]:
    return {string: len(string) for string in strings}
print(str_lengths(['hello', 'world', 'python']))
