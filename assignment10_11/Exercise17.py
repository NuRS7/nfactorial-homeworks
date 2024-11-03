"""
Exercise-17: Recursive List Sum
Write a function "recursive_sum(my_list: list) -> int" that recursively computes the sum of a list of integers.

Example:
recursive_sum([1, 2, 3, 4, 5]) -> 15
"""

def recursive_sum(my_list: list) -> int:
    if len(my_list) == 0:
        return 0
    else:
        return my_list[0] + recursive_sum(my_list[1:])
print(recursive_sum([1, 2, 3, 4, 5]))