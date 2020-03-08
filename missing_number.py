"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2
"""


def missingNumber(nums):
    gauss = len(nums)*(len(nums)+1) // 2
    return gauss - sum(nums)


nums = [3, 0, 1]
print(missingNumber(nums))
