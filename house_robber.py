"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that 
adjacent houses have security system connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""


def rob(nums):
    """
    Using DP programming -- store the results of subproblems
                            reduces time complexities from O(2^n) to O(n^2)
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    amount = [nums[0], max(nums[:2])]
    for i in range(2, len(nums)):
        amount.append(max(nums[i] + amount[i-2], amount[i-1]))

    return amount[-1]


nums = [2, 7, 9, 3, 1]
print(rob(nums))
