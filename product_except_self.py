"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""


def productExceptSelf(nums):
    ''' Left and Right product lists '''
    ans = []
    edge = 1
    # add 1 to left of [1, 2, 3, 4] -> then result in [1, 1, 2, 6]
    for num in nums:
        ans.append(edge)
        edge *= num

    edge = 1
    # add 1 to right of [1, 2, 3, 4] -> then result in [24, 12, 4, 1]
    # then mulitply each at the same index, result in [24, 12, 8, 6]
    for i in range(len(nums)-1, -1, -1):
        ans[i] = (edge*ans[i])
        edge *= nums[i]

    return ans


nums = [0, 1]
print(productExceptSelf(nums))
