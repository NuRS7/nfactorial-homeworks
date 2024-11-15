"""
Exercise-10: Dictionary Comprehension to Invert a Dictionary
Write a function "invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]" that uses a dictionary comprehension to invert a dictionary.

Example:
invert_dict({'a': 1, 'b': 2, 'c': 3}) -> {1: 'a', 2: 'b', 3: 'c'}
"""
from typing import Dict, List, Any
def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:

    return {value: key for key, value in d.items()}
print(invert_dict({'a': 1, 'b': 2, 'c': 3}))