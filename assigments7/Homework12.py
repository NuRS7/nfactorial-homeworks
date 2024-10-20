"""
Exercise-12: sum_of_multiples
Write a function "sum_of_multiples(n: int, x: int, y: int) -> int" that
takes three integers 'n', 'x', and 'y', and returns the sum of all the
numbers from 1 to 'n' (inclusive) that are multiples of 'x' or 'y'.

Example:
sum_of_multiples(10, 3, 5) -> 33
sum_of_multiples(20, 7, 11) -> 168
"""


def sum_of_multiples(n: int, x: int, y: int) -> int:
    all_total = 0
    for i in range(1, n + 1):
        if i % x == 0 or i % y == 0:
            all_total += i
    return all_total


print(sum_of_multiples(10, 3, 5))
print(sum_of_multiples(20, 7, 11))
