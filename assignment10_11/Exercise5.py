"""
Exercise-5: Decorator for Timing
Write a decorator function "timeit_decorator(func)" that prints the time taken by the function to execute.

Example:
@timeit_decorator
def sample_func():
    return [i**2 for i in range(10000)]
"""

import time




def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print(f"Function {func.__name__} executed in {exec_time} seconds to execute.")
        return result
    return wrapper
@timeit_decorator
def sample_func():
    return [i**2 for i in range(10000)]
sample_func()
print(sample_func())
