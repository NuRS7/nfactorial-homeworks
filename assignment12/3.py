"""
Exercise-3: Dictionary Comprehension to Count Characters
Write a function "char_counts(text: str) -> Dict[str, int]" that uses a dictionary comprehension to count the occurrence of each character in a string.

Example:
char_counts("hello") -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""
from typing import Dict
def char_counts(text: str) -> Dict[str, int]:
    txt={}
    for char in text:
        txt[char]=txt.get(char, 0) + 1
    return txt
print(char_counts('hello'))