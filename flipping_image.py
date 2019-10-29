def flipAndInvertImage(matrix):
    flip = []
    for items in matrix:
        flip.append(items[::-1])

    for i in range(len(flip)):
        for j in range(len(flip[i])):
            if flip[i][j] == 1:
                flip[i][j] = 0
            else:
                flip[i][j] = 1
    return flip


matrix = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
print(flipAndInvertImage(matrix))
