"""
Exercise-9: Swap dictionary keys and values
Write a function "swap_dict(d: dict) -> dict" that takes a dictionary
and returns a new dictionary where keys become values and values become keys.
if you face duplicates, the first key should be saved.

Example:
swap_dict({1: 'a', 2: 'b', 3: 'c'}) -> {'a': 1, 'b': 2, 'c': 3}
"""

def swap_dict(d: dict) -> dict:
    result_dict = dict()

    for key, value in d.items():
        if value not in result_dict:
            result_dict[value] = key
    return result_dict
    pass
print(swap_dict({1: 'a', 2: 'b', 3: 'c'}))
