"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
"""


def shiftGrid(grid, k):
    m = len(grid)
    n = len(grid[0])
    move = k % (m * n)
    if move == 0:
        return grid
    else:
        shift = []
        tmp = [j for i in grid for j in i]
        # rearrange position after moving k times
        tmp = tmp[m*n-move:] + tmp[:m*n-move]
        # slice chunk by lenght of n, which is row
        for i in range(0, len(tmp), n):
            shift.append(tmp[i:i+n])

    return shift


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 9
print(shiftGrid(grid, k))
