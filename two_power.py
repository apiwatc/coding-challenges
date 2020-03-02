"""
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true
Explanation: 20 = 1
"""


def isPowerofTwo(n):
    if n <= 0:
        return False
    elif n == 1:
        return True
    else:
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                return False
        return True


n = 1
print(isPowerofTwo(n))
