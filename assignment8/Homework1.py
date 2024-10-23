"""
Exercise-1: Count unique elements
Write a function "count_unique_elements(my_list: list) -> int" that takes a
list of integers and returns the number of unique elements in the list.
Example:
count_unique_elements([1, 2, 3, 1, 2, 4, 5, 4]) -> 5
"""

def count_unique_elements(my_list: list) -> int:
    unique_elements = set(my_list)
    return len(unique_elements)
print(count_unique_elements([1, 2, 3, 1, 2, 4, 5, 4]))