"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

XOR
1. Any number XOR itself is zero. This is sometimes used in machine code to clear a register.
2. If you XOR by the same number twice, you get the original value back. In other words, (𝑛⊻𝑦)⊻𝑦=𝑛.
   This has been used for cheesy encryption schemes and for some old-school computer graphics effects.
"""


def singleNumber(nums):
    single = 0
    for num in nums:
        single ^= num
    return single


nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))
