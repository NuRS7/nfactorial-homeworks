"""
Exercise-16: Generator to Yield Reversed List
Write a function "reverse_gen(lst: List[Any]) -> Generator[Any]" that returns a generator which yields elements from the list in reverse order.

Example:
list(reverse_gen([1, 2, 3, 4, 5])) -> [5, 4, 3, 2, 1]
"""
from typing import List, Any, Generator


def reverse_gen(lst: List[Any]) -> Generator[Any, None, None]:
    return (i for i in lst[::-1])
print(list(reverse_gen([1, 2, 3, 4, 5])))
