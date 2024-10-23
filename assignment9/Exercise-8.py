"""
Exercise-8: Count elements in range
Write a function "count_in_range(my_list: list, start: int, end: int) -> int" that
takes a list of integers and two integers as range boundaries and
returns the count of unique elements within that range in the list.

Example:
count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4) -> 3
    def test_count_in_range(self):
        self.assertEqual(hw.count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4), 3)
        self.assertEqual(hw.count_in_range([], 2, 4), 0)
        self.assertEqual(hw.count_in_range(list(range(1, 10**6+1)), 2, 4), 3)
        self.assertEqual(hw.count_in_range(list(range(1, 10**6+1)), 500000, 10**6), 500001)
        self.assertEqual(hw.count_in_range([1, 2, 3, 4, 5], 6, 10), 0)
"""

def count_in_range(my_list: list, start: int, end: int) -> int:
    elements_in_range=[num for num in my_list if start <= num <= end]
    unique_elements=set(elements_in_range)
    return len(unique_elements)



print(count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4))
print(count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4))
print(count_in_range([], 2, 4))
print(count_in_range(list(range(1, 10**6+1)), 2, 4))
print(count_in_range(list(range(1, 10**6+1)), 500000, 10**6))
print(count_in_range([1, 2, 3, 4, 5], 6, 10))
print(count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4))
print(count_in_range([1, 2, 3, 4, 5], 6, 10))