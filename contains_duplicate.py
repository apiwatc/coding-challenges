"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true
"""
import collections


def containsDuplicate(nums):
    d = collections.Counter(nums)
    for v in d.values():
        if v > 1:
            return True

    return False


nums = [1, 2, 3, 1]
print(containsDuplicate(nums))
