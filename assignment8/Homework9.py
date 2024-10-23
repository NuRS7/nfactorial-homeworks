"""
Exercise-9: Check if a list is sorted
Write a function "is_sorted(my_list: list) -> bool" that takes a list
of integers and returns True if the list is sorted in non-descending
order (i.e., each element is greater than or equal to the previous element),
False otherwise.

Example:
is_sorted([1, 2, 3, 4, 5]) -> True
is_sorted([1, 3, 2, 4, 5]) -> False
"""

def is_sorted(my_list: list) -> bool:
    return my_list == sorted(my_list)
print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 3, 2, 4, 5]))
