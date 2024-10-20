"""
Exercise-13: gcd
Write a function "gcd(a: int, b: int) -> int" that takes two integers 'a' and 'b',
and returns their greatest common divisor (GCD).

Example:
gcd(56, 98) -> 14
gcd(27, 15) -> 3
"""

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a%b
    return abs(a)
print(gcd(56, 98))
print(gcd(27, 15))
