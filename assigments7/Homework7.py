"""
Exercise-7: sum_of_squares
Write a function "sum_of_squares(n: int) -> int" that takes an integer 'n' and
returns the sum of squares of all integers from 1 to 'n'.

Example:
sum_of_squares(4) -> 30
sum_of_squares(5) -> 55
"""

def sum_of_squares(n: int) -> int:
    total = 0
    for i in range(1, n+1):
        total += i**2
    return total
print(sum_of_squares(4))
print(sum_of_squares(5))