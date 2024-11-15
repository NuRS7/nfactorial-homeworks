"""
Exercise-17: Dictionary Comprehension to Group By Length
Write a function "group_by_length(words: List[str]) -> Dict[int, List[str]]" that uses a dictionary comprehension to group words by their length.

Example:
group_by_length(['hello', 'world', 'python', 'is', 'fun']) -> {5: ['hello', 'world'], 6: ['python'], 2: ['is'], 3: ['fun']}
"""
from typing import Dict, List
def group_by_length(words: List[str]) -> Dict[int, List[str]]:
    # return {len(word): [word] for word in words} в начале осылай ойладым
    return {length: [word for word in words if len(word) == length] for length in set(len(word) for word in words)}
print(group_by_length(['hello', 'world', 'python', 'is', 'fun']))