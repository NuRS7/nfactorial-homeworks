"""
Exercise-11: Prime Numbers with List Comprehension
Write a function "primes(n: int) -> List[int]" that uses a list comprehension to return a list of all prime numbers up to 'n'.

Example:
primes(10) -> [2, 3, 5, 7]
"""
from typing import List


def primes(n: int) -> List[int]:
    return [i for i in range(2, n) if all(i % j != 0 for j in range(2, i))]
print(list(primes(10)))



