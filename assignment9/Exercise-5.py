"""
Exercise-5: Character frequency
Write a function "char_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each character in the string.

Example:
char_frequency('hello world') -> {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
"""


def char_frequency(my_string: str) -> dict:
    return dict((char, my_string.count(char)) for char in set(my_string))

print(char_frequency('hello world'))
