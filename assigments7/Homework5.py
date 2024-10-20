"""Exercise-5: sum_of_digits
Write a function "sum_of_digits(n: int) -> int" that
takes an integer 'n' and returns the sum of its digits.

Example:
sum_of_digits(12345) -> 15
sum_of_digits(98765) -> 35
"""

def sum_of_digits(n: int) -> int:
    return sum(int(digit) for digit in str(n))
print(sum_of_digits(12345))
print(sum_of_digits(98765))