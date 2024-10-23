"""
Exercise-13: Most frequent element
Write a function "most_frequent(my_list: list) -> int" that takes a
list of integers and returns the most frequent element in the list.

Example:
most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]) -> 1
"""

def most_frequent(my_list: list) -> int:
    return max(set(my_list), key=my_list.count)
print(most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]))
