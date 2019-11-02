"""
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums, target):
    hash_table = {}
    for i, j in enumerate(nums):
        if target - nums[i] in hash_table:
            return hash_table[target-nums[i]], i
        else:
            hash_table[nums[i]] = i
