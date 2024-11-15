"""
Exercise-4: Generator of Generators
Write a function "generators(n: int) -> Generator[Generator[int]]" that creates a generator which yields 'n' number of generators.
Each of these generators yields numbers from 1 to 'n'.

Example:
list(map(list, generators(3))) -> [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
"""
from typing import Generator
def generators(n: int) -> Generator[Generator[int, None, None], None, None]:
    for _ in range(n):
        def gen():
            for i in range(1, n + 1):
                yield i
        yield gen()
print(list(map(list, generators(3))))