"""
On an 8 x 8 chessboard, there is one white rook.
There also may be empty squares, white bishops, and black pawns.
These are given as characters 'R', '.', 'B', and 'p' respectively.
Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south),
then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
"""


def numRookCaptures(board):
    NS = []
    EW = []
    R = []
    p = []
    B = []
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                R += [i]+[j]
            if board[i][j] == 'p':
                p += [[i, j]]
            if board[i][j] == 'B':
                B += [[i, j]]

    # Possibility move for Rook
    # Put Rook in both direction
    for i in range(8):
        NS.append([i, R[1]])
        EW.append([R[0], i])
        if R == NS[i]:
            NS[i] = 'R'
        if R == EW[i]:
            EW[i] = 'R'

    for i in range(8):
        for j in range(len(p)):
            if NS[i] == p[j]:
                NS[i] = 'p'
            if EW[i] == p[j]:
                EW[i] = 'p'

    for i in range(8):
        for j in range(len(B)):
            if B[j] == NS[i]:
                NS[i] = 'B'
            if B[j] == EW[i]:
                EW[i] = 'B'

    index = NS.index('R')
    for i in range(index, 0, -1):
        if NS[i] == 'B':
            break
        if NS[i] == 'p':
            count += 1
            break
    for i in range(index+1, 8):
        if NS[i] == 'B':
            break
        if NS[i] == 'p':
            count += 1
            break

    index = EW.index('R')
    for i in range(index, 0, -1):
        if EW[i] == 'B':
            break
        if EW[i] == 'p':
            count += 1
            break
    for i in range(index+1, 8):
        if EW[i] == 'B':
            break
        if EW[i] == 'p':
            count += 1
            break

    return count


board = [[".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         ["p", "p", ".", "R", ".", "p", "B", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "B", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."]]
print(numRookCaptures(board))
