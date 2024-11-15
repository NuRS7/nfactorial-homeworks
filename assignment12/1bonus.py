"""
Exercise-1: Prime Sieve with List Comprehension
Write a function "sieve_of_eratosthenes(n: int) -> List[int]" that implements the Sieve of Eratosthenes to generate all prime numbers less than 'n'.
Use a list comprehension to generate the initial list of numbers, and another to remove multiples of each prime found.

Example:
sieve_of_eratosthenes(30) -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
"""
from typing import List
def sieve_of_eratosthenes(n: int) -> List[int]:
    return [i for i in range(2, n) if all(i % j != 0 for j in range(2, i))]
print(sieve_of_eratosthenes(30))