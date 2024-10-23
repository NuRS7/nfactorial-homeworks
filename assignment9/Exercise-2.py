"""Exercise-2: Count occurrences
Write a function "count_occurrences(my_list: list) -> dict" that takes a
list of integers and returns a dictionary where keys are unique integers
from the list and values are their counts in the list.

Example:
count_occurrences([1, 2, 3, 1, 2, 4, 5, 4]) -> {1: 2, 2: 2, 3: 1, 4: 2, 5: 1}
"""
def count_occurrences(my_list: list) -> dict:
    return {key: my_list.count(key) for key in set(my_list)}
print(count_occurrences([1, 2, 3, 1, 2, 4, 5, 4]))