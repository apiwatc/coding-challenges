"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [a, b] = [nums[2*i], nums[2*i+1]] (with i >= 0).
For each such pair, there are a elements with value b in the decompressed list.

Return the decompressed list.

Example 1:
Input: nums = [1,2,3,4]
Output: [2,4,4,4]
"""


def decompressRLElist(nums):
    decompress = []
    for i in range(0, len(nums), 2):
        decompress.extend(nums[i] * [nums[i + 1]])  # [4] * 2 = [4, 4]
    return decompress


nums = [1, 2, 3, 39]
print(decompressRLElist(nums))
