"""
Exercise-16: digit_count
Write a function "digit_count(n: int) -> int" that takes an
integer 'n' and returns the number of digits in 'n'.

Example:
digit_count(123) -> 3
digit_count(4567) -> 4
"""

def digit_count(n: int) -> int:
    return len(str(abs(n))) # абс минус сандар болмауы ушн
print(digit_count(123))
print(digit_count(4567))
