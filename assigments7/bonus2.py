"""
💎 Exercise-2: find_smallest_divisor
Write a function "find_smallest_divisor(n: int) -> int" that
takes a positive integer 'n' and returns the smallest prime divisor of 'n'.

Example:
find_smallest_divisor(21) -> 3
find_smallest_divisor(49) -> 7
"""

def find_smallest_divisor(n: int) -> int:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
print(find_smallest_divisor(21))
print(find_smallest_divisor(49))