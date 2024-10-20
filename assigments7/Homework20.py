"""
Exercise-20: is_armstrong_number
Write a function "is_armstrong_number(n: int) -> bool" that takes an
integer 'n' and returns True if 'n' is an Armstrong number, and False otherwise.

Example:
is_armstrong_number(153) -> True
is_armstrong_number(370) -> True
"""

def is_armstrong_number(n: int) -> bool:
    str_n = str(n)
    length = len(str_n)
    result = 0
    for i in str_n:
        result += int(i) ** length
    return result == n
print(is_armstrong_number(153))
print(is_armstrong_number(370))
