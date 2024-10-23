"""
Exercise-3: Reverse a list
Write a function "reverse_list(my_list: list) -> list" that takes a list of integers and
returns a new list with the elements in reverse order.

Example:
reverse_list([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
"""

def reverse_list(my_list: list) -> list:
    return my_list[::-1]
print(reverse_list([1, 2, 3, 4, 5]))