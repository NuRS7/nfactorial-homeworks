"""
Exercise-13: Decorator for Function Counting
Write a decorator function "count_calls(func)" that counts the number of times a function is called.

Example:
@count_calls
def test_function():
    return

test_function()
test_function()
# Output: 'test_function' was called 2 times.
"""

def count_calls(func):
 def wrapper(*args, **kwargs):
    wrapper.count += 1
    return func(*args, **kwargs)
 wrapper.count = 0
 return wrapper

@count_calls
def test_function():
    return

test_function()
test_function()
