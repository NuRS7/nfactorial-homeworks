"""
Exercise-9: is_leap_year
Write a function "is_leap_year(year: int) -> bool" that takes an
integer 'year' and returns True if 'year' is a leap year, and False otherwise.

Example:
is_leap_year(2000) -> True
is_leap_year(1900) -> False
"""

def is_leap_year(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
print(is_leap_year(1900))
print(is_leap_year(2000))