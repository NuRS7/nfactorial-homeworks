"""
Exercise-10: Count the frequency of an element in a list
Write a function "count_frequency(my_list: list, element: int) -> int" that
takes a list of integers and an element, and returns the number of
times the element appears in the list.

Example:
count_frequency([1, 2, 3, 4, 5, 1, 2, 3], 3) -> 2
"""

def count_frequency(my_list: list, element: int) -> int:
    return my_list.count(element)
print(count_frequency([1,2,3,4,5,1,2,3],3))