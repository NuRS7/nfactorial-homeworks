"""
Exercise-19: is_perfect_square
Write a function "is_perfect_square(n: int) -> bool" that takes an
integer 'n' and returns True if 'n' is a perfect square, and False otherwise.

Example:
is_perfect_square(9) -> True
is_perfect_square(10) -> False
"""
import math
def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    square = math.sqrt(n)
    return square.is_integer()
print(is_perfect_square(9))
print(is_perfect_square(10))