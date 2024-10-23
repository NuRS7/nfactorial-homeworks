"""
Exercise-4: Find the maximum value in a list
Write a function "max_value(my_list: list) -> int" that takes a
list of integers and returns the maximum value in the list.

Example:
max_value([1, 2, 3, 4, 5]) -> 5
"""

def max_value(my_list: list) -> int:
    list_length = len(my_list)
    max_value = my_list[0]
    for i in range(1, list_length):
        if my_list[i] > max_value:
            max_value = my_list[i]
    return max_value
print(max_value([1, 2, 3, 4, 5]))