"""
Exercise-16: Find the union of two lists
Write a function "find_union(list1: list, list2: list) -> list" that takes
two lists of integers and returns a new list with the elements that are
present in either list (i.e., the union of the lists).

Example:
find_union([1, 2, 3, 4], [3, 4, 5, 6]) -> [1, 2, 3, 4, 5, 6]
"""

def find_union(list1: list, list2: list) -> list:
     return list(set(list1) | set(list2))
print(find_union([1, 2, 3, 4], [3, 4, 5, 6]))