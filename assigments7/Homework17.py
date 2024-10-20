"""
Exercise-17: is_power_of_two
Write a function "is_power_of_two(n: int) -> bool" that takes an integer 'n'
and returns True if 'n' is a power of 2, and False otherwise.

Example:
is_power_of_two(8) -> True
is_power_of_two(10) -> False
"""

def is_power_of_two(n: int) -> bool:
    if n <= 0 :
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True
print(is_power_of_two(8))
print(is_power_of_two(10))