"""
Exercise-14: Least frequent element
Write a function "least_frequent(my_list: list) -> int" that takes a
list of integers and returns the least frequent element in the list.

Example:
least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]) -> 3
"""

def least_frequent(my_list: list) -> int:
    return min(set(my_list), key=my_list.count)
print(least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]))
