"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


def subsets(nums):
    subs = [[]]
    for i in range(len(nums)):
        # len(subs) updates once subs appends new value
        for j in range(len(subs)):
            subs += [subs[j] + [nums[i]]]

    return subs


nums = [1, 2, 3]
print(subsets(nums))
