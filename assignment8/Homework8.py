"""
Exercise-8: Find the index of an element in a list
Write a function "find_index(my_list: list, element: int) -> int" that takes a
list of integers and an element, and returns the index of the first occurrence of
the element in the list. If the element is not in the list, return -1.

Example:
find_index([1, 2, 3, 4, 5], 3) -> 2
find_index([1, 2, 3, 4, 5], 6) -> -1
"""

def find_index(my_list: list, element: int) -> int:
    for index, value in enumerate(my_list):
        if value == element:
            return index
    return -1
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5], 6))