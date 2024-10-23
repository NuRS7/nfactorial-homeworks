"""
Exercise-2: Remove duplicates
Write a function "remove_duplicates(my_list: list) -> list" that takes a list of integers and
removes all duplicates, returning the new list with unique elements in their original order.

Example:
remove_duplicates([1, 2, 3, 1, 2, 4, 5, 4]) -> [1, 2, 3, 4, 5]
"""
my_list =([1, 2, 3, 1, 2, 4, 5, 4])
def remove_duplicates(my_list: list) -> list:
    return list(set(my_list))
print(remove_duplicates(my_list))