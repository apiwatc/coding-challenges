"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i, j = 0, len(nums)-1

    if 0 not in nums:
        return
    # j = number of ZERO, won't keep swapping ZERO with ZERO
    while i < len(nums) and i < j:
        if nums[i] == 0:
            nums.append(nums.pop(i))
            j -= 1
        else:
            i += 1


nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))
print(nums)
