"""
💎 Exercise-1: count_substrings
Write a function "count_substrings(s: str, subs: str) -> int" that takes
two strings 's' and 'subs' and returns the number of non-overlapping
occurrences of the substring 'subs' in the string 's'.

Example:
count_substrings("ababab", "ab") -> 3
count_substrings("aaaaaa", "aa") -> 3
"""

def count_substrings(s: str, subs: str) -> int:
    a =s.count(subs)
    return a
print(count_substrings("ababab", "ab"))
print(count_substrings("aaaaaa", "aa"))
