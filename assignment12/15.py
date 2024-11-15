"""
Exercise-15: Nested List Comprehension to Transpose Matrix
Write a function "transpose(matrix: List[List[Any]]) -> List[List[Any]]" that uses a nested list comprehension to transpose a matrix.

Example:
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""


from typing import List, Any
def transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# киын екен