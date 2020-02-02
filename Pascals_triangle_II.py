"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]
"""


def getRow(rowIndex):
    pascal = [[1], [1, 1]]
    if rowIndex <= 1:
        return pascal[rowIndex]

    for i in range(1, rowIndex):
        tmp = [1]
        for j in range(i):
            tmp.append(pascal[i][j] + pascal[i][j+1])
        tmp.append(1)
        pascal.append(tmp)
    return pascal[-1]


rowIndex = 3
print(getRow(rowIndex))
