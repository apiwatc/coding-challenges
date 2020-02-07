"""
There are some chips, and the i-th chip is at position chips[i].

You can perform any of the two following types of moves any number of times (possibly zero) on any chip:
    Move the i-th chip by 2 units to the left or to the right with a cost of 0.
    Move the i-th chip by 1 unit to the left or to the right with a cost of 1.

There can be two or more chips at the same position initially.
Return the minimum cost needed to move all the chips to the same position (any position).

Example 1:
Input: chips = [1,2,3]
Output: 1
Explanation: Second chip will be moved to positon 3 with cost 1. First chip will be moved to position 3 with cost 0. Total cost is 1.
"""


def minCostToMoveChips(chips):
    even_move = 0
    odd_move = 0
    for pos in chips:
        if pos % 2 == 0:
            even_move += 1
        else:
            odd_move += 1
    return min(even_move, odd_move)


chips = [2, 2, 2, 3, 3]
print(minCostToMoveChips(chips))
