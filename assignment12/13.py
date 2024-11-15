"""
Exercise-13: Generator Expression to Yield Factorials
Write a function "factorials_gen(n: int) -> Generator[int]" that uses a generator expression to yield the factorials of all numbers up to 'n'.

Example:
list(factorials_gen(5)) -> [1, 2, 6, 24, 120]
"""
from math import factorial
from typing import Generator


def factorials_gen(n: int) -> Generator[int, None, None]:
    return (factorial(i) for i in range(1, n + 1))
print(list(factorials_gen(5)))