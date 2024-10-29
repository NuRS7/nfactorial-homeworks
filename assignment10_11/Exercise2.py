"""
Exercise-2: Implement Map Function
Write a function "my_map(func, my_list: list) -> list" that mimics the built-in Python 'map' function. It should take a function and a list as input, applying the function to each element of the list.

Example:
my_map(lambda x: x**2, [1, 2, 3, 4]) -> [1, 4, 9, 16]
"""

def my_map(func, my_list: list) -> list:
    return [func(x) for x in my_list]
    my_map(lambda x: x**2, [1, 2, 3, 4])
print(my_map(lambda x: x**2, [1, 2, 3, 4]))