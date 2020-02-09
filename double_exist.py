"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

    - i != j
    - 0 <= i, j < arr.length
    - arr[i] == 2 * arr[j]
 
Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
"""


def checkIfExist(arr):
    nums = set(arr)
    if 0 in nums and len(nums) == 1:
        return True
    for num in nums:
        if 2*num in nums and num != 0:
            return True
    return False


arr = [0, 0, 2, 3]
print(checkIfExist(arr))
