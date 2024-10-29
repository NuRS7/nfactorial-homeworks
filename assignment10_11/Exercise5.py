"""
Exercise-5: Decorator for Timing
Write a decorator function "timeit_decorator(func)" that prints the time taken by the function to execute.

Example:
@timeit_decorator
def sample_func():
    return [i**2 for i in range(10000)]
"""


def timeit_decorator(func):
    def wrapper():
        pass
    return wrapper

@timeit_decorator
def sample_func():
    return [i**2 for i in range(10000)]
print(sample_func())