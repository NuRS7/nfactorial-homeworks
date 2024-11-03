"""
Exercise-6: Function Composition
Write a function "compose(*funcs)" that takes a series of functions and returns a new function that composes them. The returned function should take an input and apply each function to the result of the previous function.

Example:
def double(x):
    return 2 * x
def square(x):
    return x ** 2
new_func = compose(double, square)
new_func(3) -> 36
"""

def compose(*funcs):
    def new_func(x):
        result = x
        for func in funcs:
            result = func(result)
        return result
    return new_func
print(compose(lambda x: x * 2, lambda x: x ** 2)(3))

