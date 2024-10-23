"""
Exercise-17: Find the difference of two lists
Write a function "find_difference(list1: list, list2: list) -> list" that takes
two lists of integers and returns a new list with the elements that are
present in the first list but not the second list.
Assume that list does not contain duplicates.

Example:
find_difference([1, 2, 3, 4], [3, 4, 5, 6]) -> [1, 2]
"""

def find_difference(list1: list, list2: list) -> list:
    return  list(set(list1) - set(list2))
print(find_difference([1, 2, 3, 4], [3, 4, 5, 6]))