"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
    Given input matrix = 
    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ],

    rotate the input matrix in-place such that it becomes:
    [
    [7,4,1],
    [8,5,2],
    [9,6,3]
    ]
"""


import copy


def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    tmp = copy.deepcopy(matrix)
    idx = len(matrix)-1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = tmp[(len(matrix)-1)-j][i]


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(rotate(matrix))
print(matrix)
