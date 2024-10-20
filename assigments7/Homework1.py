"""Exercise-1: is_prime
Write a function "is_prime(n: int) -> bool" that takes an integer 'n'
and checks whether it is prime. Function should return a boolean value.

Example:
is_prime(7) -> True
is_prime(10) -> False
"""

def is_prime(n: int) -> bool:
    if n < 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
    pass
print(is_prime(7))
print(is_prime(10))