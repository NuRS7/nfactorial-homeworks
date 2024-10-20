"""
Exercise-3: factorial
Write a function "factorial(n: int) -> int" that takes an integer 'n' and returns the factorial of 'n'.

Example:
factorial(5) -> 120
factorial(6) -> 720
"""

def factorial(n: int) -> int:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
i = int(input("Enter a number: "))
print("factorial({}) = {}".format(i, factorial(i)))