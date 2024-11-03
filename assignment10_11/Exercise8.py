"""
Exercise-8: Reduce to Compute Factorial
Write a function "factorial_reduce(n: int) -> int" that uses `reduce` to compute the factorial of an integer.

Example:
factorial_reduce(5) -> 120
"""
from functools import reduce
def partial(func, *args):
    def new_func(*new_args):
        return func(*args, *new_args)
    return new_func

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial_reduce(5))