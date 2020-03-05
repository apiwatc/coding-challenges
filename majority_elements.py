"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3
"""
import collections


def majorityElement(nums):
    d = collections.Counter(nums)
    return d.most_common(1)[0][0]


nums = [1, 1, 2, 2, 3, 3, 3]
print(majorityElement(nums))
