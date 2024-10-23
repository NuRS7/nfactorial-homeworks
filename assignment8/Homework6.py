"""
Exercise-6: Sum all values in a list
Write a function "sum_values(my_list: list) -> int" that takes a
list of integers and returns the sum of all values in the list.

Example:
sum_values([1, 2, 3, 4, 5]) -> 15
"""

def sum_values(my_list: list) -> int:
    total = 0
    for i in my_list:
        total += i
    return total
print(sum_values([1,2,3,4,5]))