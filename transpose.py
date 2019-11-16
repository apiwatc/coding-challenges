"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, 
switching the row and column indices of the matrix.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
"""


def transpose(A):
    transpose = []
    for i in range(len(A[0])):
        arr = []
        for j in range(len(A)):
            arr += [A[j][i]]
        transpose.append(arr)
    return transpose


matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose(matrix))
