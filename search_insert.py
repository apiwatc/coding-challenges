"""
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2
"""
import time


def searchInsert(nums, target):
    low = 0
    high = len(nums)-1

    if target in nums:
        return nums.index(target)
    else:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            while low <= high:
                if target < nums[-1]:
                    mid = (low + high) // 2
                    # Check if target is present at mid
                    if nums[mid] == target:
                        return mid
                    # If target is greater, ignore the left half
                    elif target > nums[mid]:
                        low = mid + 1
                    # If target is smaller, ignore the right half
                    else:
                        high = mid - 1
            return low


nums = [3, 6, 7, 8, 10]
target = 5
start = time.time()
print(searchInsert(nums, target))
print((time.time()-start)*1000)
