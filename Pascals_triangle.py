"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]
"""
# [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
# when i = 0     1         2          3


def generate(numRows):
    pascal = [[1], [1, 1]]
    if numRows <= 2:
        return pascal[:numRows]
    # only to the second list to calculate, so start from 1 and need only numRows-2 elements
    for i in range(1, numRows-1):
        # always add first ele
        tmp = [1]
        # middle elements begin here
        for j in range(i):
            # ele at index 1 of next list = ele at index 0 + ele at index 1 of previous list
            tmp.append(pascal[i][j] + pascal[i][j+1])
        # always add last ele
        tmp.append(1)
        pascal.append(tmp)
    return pascal


numRows = 5
print(generate(numRows))
