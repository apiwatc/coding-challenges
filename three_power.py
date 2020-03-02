"""
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true
"""


def isPowerOfThree(n):
    if n <= 0:
        return False
    if n == 1:
        return True

    while n > 1:
        if n % 3 == 0:
            n //= 3
        else:
            return False
    return True


n = 27
print(isPowerofTwo(n))
