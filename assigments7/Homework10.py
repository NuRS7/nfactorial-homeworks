"""
Exercise-10: count_words
Write a function "count_words(s: str) -> int" that takes a string 's' and
returns the number of words in the string. Assume words are separated by spaces.

Example:
count_words("Hello world") -> 2
count_words("This is a test") -> 4
"""

def count_words(s: str) -> int:
    words = s.split()
    return len(words)
print(count_words("Hello world"))
print(count_words("This is a test"))
