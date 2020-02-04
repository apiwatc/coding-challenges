"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
"""


def sumZero(n):
    if n % 2 != 0:
        return list(range((n//2)+1)) + list(range(-(n//2), 0))
    else:
        return list(range(1, (n//2)+1)) + list(range(-(n//2), 0))


n = 3
print(sumZero(n))
