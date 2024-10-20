"""Example:
reverse_string("hello") -> "olleh"
reverse_string("world") -> "dlrow"
"""


def reverse_string(s: str) -> str:
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string
print(reverse_string("hello"))
