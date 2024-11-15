"""
Exercise-6: Set Comprehension to Find Odd Squares
Write a function "odd_squares(n: int) -> Set[int]" that uses a set comprehension to find the squares of all odd numbers up to 'n'.

Example:
odd_squares(10) -> {1, 9, 25, 49, 81}
"""
def odd_squares(n: int) -> set[int]:
    return { i**2 for i in range(1, n+1) if i % 2 != 0 }

res = sorted(odd_squares(10))
print(res)