
"""
Exercise-10: Subset check
Write a function "is_subset(set1: set, set2: set) -> bool" that takes two
sets and returns True if set2 is a subset of set1, and False otherwise.

Example:
is_subset({1, 2, 3, 4, 5}, {3, 4, 5}) -> True
  def test_is_subset(self):
        self.assertEqual(hw.is_subset({1, 2, 3, 4, 5}, {3, 4, 5}), True)
        self.assertEqual(hw.is_subset({1, 2, 3}, {4, 5, 6}), False)
        self.assertEqual(hw.is_subset(set(), {1, 2, 3}), False)
        self.assertEqual(hw.is_subset({i for i in range(1, 10**6+1)}, {i for i in range(500000, 10**6+1)}), True)
        self.assertEqual(hw.is_subset({1, 2, 3}, {1, 2, 3}), True)

"""

def is_subset(set1: set, set2: set) -> bool:
    return set2.issubset(set1)
print(is_subset({1, 2, 3, 4, 5}, {3, 4, 5}))
