"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci].
For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

Example 1:
Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
"""


def oddCells(n, m, indices):
    row = [0] * n
    col = [0] * m
    for r, c in indices:
        row[r] += 1
        col[c] += 1

    return len([i+j for i in col for j in row if (i+j) % 2 != 0])


n = 2
m = 3
indices = [[0, 1], [1, 1]]
print(oddCells(n, m, indices))
