"""
Exercise-7: Find the average of a list
Write a function "average(my_list: list) -> float" that takes a
list of integers and returns the average value of the list.

Example:
average([1, 2, 3, 4, 5]) -> 3.0
"""

def average(my_list: list) -> float:
    return sum(my_list) / len(my_list)
print(average([1, 2, 3, 4, 5]))