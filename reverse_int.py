"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
"""


def reverse(x):
    rev = 0
    num = abs(x)
    while num != 0:
        rev = (rev * 10) + (num % 10)
        num = num // 10

    if x < 0:
        rev *= -1

    if (-2**31) < rev < (2**31)-1:
        return rev

    return 0


x = 0
print(reverse(x))
