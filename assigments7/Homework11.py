"""
Exercise-11: is_palindrome
Write a function "is_palindrome(s: str) -> bool" that takes a string 's' and 
checks if the string is a palindrome. The function should return True if the 
string is a palindrome, and False otherwise.

Example:
is_palindrome("racecar") -> True
is_palindrome("hello") -> False
"""

def is_palindrome(s: str) -> bool:
    result = s.lower()
    return result == result[::-1]
print(is_palindrome("racecar"))
print(is_palindrome("hello"))