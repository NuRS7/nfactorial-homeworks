"""
Exercise-14: lcm
Write a function "lcm(a: int, b: int) -> int" that takes two integers 'a' and 'b',
and returns their least common multiple (LCM).

Example:
lcm(5, 7) -> 35
lcm(6, 8) -> 24
"""

def lcm(a: int, b: int) -> int:
    numbers= max(a, b)
    while True:
        if numbers % a == 0 and numbers % b == 0:
            return numbers
        numbers +=1
print(lcm(5, 7 ) )
print(lcm(6, 8))
