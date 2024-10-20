"""
Exercise-18: sum_of_cubes
Write a function "sum_of_cubes(n: int) -> int" that takes an integer 'n'
and returns the sum of the cubes of all numbers from 1 to 'n'.

Example:
sum_of_cubes(3) -> 36
sum_of_cubes(4) -> 100
"""

def sum_of_cubes(n: int) -> int:
    total = 0
    for i in range(1, n+1):
        total += i**3
    return total
print(sum_of_cubes(3))
print(sum_of_cubes(4))
