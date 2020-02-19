def countNegatives(grid):
    count = 0
    for row in grid:
        for i in range(len(row)):
            if row[i] < 0:
                count += len(row) - i
                break

    return count


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(countNegatives(grid))
