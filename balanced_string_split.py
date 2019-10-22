"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", 
            each substring contains same number of 'L' and 'R'.
"""


def balancedStringSplit(s):
    count = 0
    rcount = 0
    lcount = 0
    for x in s:
        if x == 'R':
            rcount += 1
        if x == 'L':
            lcount += 1
        if rcount == lcount:
            count += 1
    return count
