"""
Exercise-5: Find the minimum value in a list
Write a function "min_value(my_list: list) -> int" that takes a
list of integers and returns the minimum value in the list.

Example:
min_value([1, 2, 3, 4, 5]) -> 1
"""

def min_value(my_list: list) -> int:
    return min(my_list)
    min_value = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] < min_value:
            min_value = my_list[i]
    return min_value
print(min_value([1,2,3,4,5]))