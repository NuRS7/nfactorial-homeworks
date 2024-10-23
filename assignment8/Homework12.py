"""
Exercise-12: Remove all occurrences of an element in a list
Write a function "remove_all(my_list: list, element: int) -> list"
that takes a list of integers and an element, and returns a new list
with all occurrences of the element removed.

Example:
remove_all([1, 2, 3, 4, 5, 1, 2, 3], 3) -> [1, 2, 4, 5, 1, 2]
"""

def remove_all(my_list: list, element: int) -> list:
    while element in my_list:
        my_list.remove(element)
    return my_list
print(remove_all([1, 2, 3, 4, 5, 1, 2, 3], 3))

