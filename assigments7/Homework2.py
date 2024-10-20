"""
Exercise-2: nth_fibonacci
Write a function "nth_fibonacci(n: int) -> int" that
takes an integer 'n' and returns the nth number in the Fibonacci sequence.

Example:
nth_fibonacci(6) -> 5
nth_fibonacci(9) -> 21
"""

def nth_fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
    pass

print(nth_fibonacci(5))
print(nth_fibonacci(21))