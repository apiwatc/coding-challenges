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

    if len(nums) <= 0:
        return subs
    elif len(nums) == 1:
        return [[], nums]
    for num in nums:
        # len(subs) updates once subs appends new value
        for i in range(len(subs)):
            subs += [subs[i] + [num]]

    return subs


nums = [1]
print(subsets(nums))
