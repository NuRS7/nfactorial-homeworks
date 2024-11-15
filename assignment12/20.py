"""
Exercise-20: Dictionary Comprehension to Convert List to Dict
Write a function "list_to_dict(lst: List[Any]) -> Dict[int, Any]" that uses a dictionary comprehension to convert a list into a dictionary where the keys are the indices of the list elements.

Example:
list_to_dict(['a', 'b', 'c']) -> {0: 'a', 1: 'b', 2: 'c'}
"""
from typing import List, Any, Dict
def list_to_dict(lst: List[Any]) -> Dict[int, Any]:
    return {i: lst[i] for i in range(len(lst))}
print(list_to_dict(['a', 'b', 'c']))