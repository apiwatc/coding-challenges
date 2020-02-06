"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3
"""


def singleNumber(nums):
    return ((sum(set(nums))*3) - (sum(nums))) // 2


nums = [0, 1, 0, 1, 0, 1, 99]
print(singleNumber(nums))
