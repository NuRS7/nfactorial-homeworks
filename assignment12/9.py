
"""
Exercise-9: Fibonacci Sequence with Generators
Write a function "fibonacci_gen(n: int) -> Generator[int]" that uses a generator to yield the Fibonacci sequence up to the nth term.

Example:
list(fibonacci_gen(10)) -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""
from typing import Generator

def fibonacci_gen(n: int) -> Generator[int, None, None]:
    a, b=0, 1
    for _ in range(n):
        yield a
        a, b=b, a + b
print(list(fibonacci_gen(10)))
