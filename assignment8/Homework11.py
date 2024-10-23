"""
Exercise-11: Find the mode of a list
Write a function "find_mode(my_list: list) -> int" that takes a list of 
integers and returns the mode (i.e., the value that appears most frequently) 
of the list. If there are multiple modes, return any of them.

Example:
find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3]) -> 2
  self.assertEqual(hw.find_mode([]), None)
"""
def find_mode(my_list: list) -> int:
    if not my_list:
        return None
    frequency = {}
    for num in my_list:
        frequency[num] = frequency.get(num, 0) + 1
    return max(frequency, key=frequency.get)
print(find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3]))
print(find_mode([]))