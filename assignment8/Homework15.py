"""
Exercise-15: Find the intersection of two lists
Write a function "find_intersection(list1: list, list2: list) -> list" that
takes two lists of integers and returns a new list with the elements that are present in both lists.

Example:
find_intersection([1, 2, 3, 4], [3, 4, 5, 6]) -> [3, 4]
"""

def find_intersection(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))
print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6]))