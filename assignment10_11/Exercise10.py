"""
Exercise-10: Custom Reduce Function
Implement your own version of Python's 'reduce' function "my_reduce(func, iterable, initializer=None)".

Example:
my_reduce(lambda x, y: x*y, [1, 2, 3, 4]) -> 24
"""
from functools import reduce


def my_reduce(func, iterable, initializer=None):
    return reduce(func, iterable)
print(my_reduce(lambda x, y: x*y, [1, 2, 3, 4]))