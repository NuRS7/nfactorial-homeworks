"""Exercise-1: Find missing elements
Write a function "missing_elements(my_list: list) -> list" that takes a
sorted list of integers and returns a list of missing integers in the range of the list.

Example:
missing_elements([1, 2, 4, 6, 7]) -> [3, 5]
"""
# def missing_elements(my_list: list) -> list:
#     return list(set(range(my_list[0], my_list[-1]+1)) - set(my_list))
# print(missing_elements([1, 2, 4, 6, 7]))

def missing_elements(my_list: list) -> list:
    if not my_list:
        return []
    full_range=range(my_list[0], my_list[-1] + 1)
    missing=[num for num in full_range if num not in my_list]
    return missing