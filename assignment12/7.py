"""
Exercise-7: Dictionary Comprehension to Map Indices
Write a function "index_map(text: str) -> Dict[str, int]" that uses a dictionary comprehension to map each character in a string to its index.

Example:
index_map("hello") -> {'h': 0, 'e': 1, 'l': 3, 'o': 4}
"""
def index_map(text: str) -> dict[str, int]:
    return {char: index for index, char in enumerate(text)}
print(index_map("hello"))
