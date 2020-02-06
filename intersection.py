"""
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""


def intersect(nums1, nums2):
    intersection = []
    count = {}
    for num in nums1:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    for num in nums2:
        if num in count and count[num] > 0:
            count[num] -= 1
            intersection.append(num)

    return intersection


nums1 = [1, 2, 2, 2, 2, 1]
nums2 = [2, 2, 2]
print(intersect(nums1, nums2))
