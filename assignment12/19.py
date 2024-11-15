"""
Exercise-19: Generator Expression to Yield Primes
Write a function "primes_gen(n: int) -> Generator[int]" that uses a generator expression to yield all prime numbers up to 'n'.

Example:
list(primes_gen(10)) -> [2, 3, 5, 7]
"""

from typing import Generator
def primes_gen(n: int) -> Generator[int, None, None]:
    return (i for i in range(2, n + 1) if all(i % j != 0 for j in range(2, i)))
print(list(primes_gen(10)))
