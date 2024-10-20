
"""
Exercise-8: collatz_sequence_length
Write a function "collatz_sequence_length(n: int) -> int" that takes an
integer 'n' and returns the length of the Collatz sequence starting with 'n'.

Example:
collatz_sequence_length(6) -> 9
collatz_sequence_length(27) -> 112
"""
from operator import length_hint


def collatz_sequence_length(n: int) -> int:
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length
print(collatz_sequence_length(6))
print(collatz_sequence_length(27))
