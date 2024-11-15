"""
Exercise-5: Generator Expression to Yield Squares
Write a function "squares_gen(n: int) -> Generator[int]" that uses a generator expression to yield the squares of all numbers up to 'n'.

Example:
list(squares_gen(5)) -> [0, 1, 4, 9, 16]
"""
from typing import Generator


def squares_gen(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i**2
print(list(squares_gen(5)))

