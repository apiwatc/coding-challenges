"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

import collections


def topKFrequent(nums, k):
    d = collections.Counter(nums).most_common(k)
    ans = []
    for i in range(len(d)):
        ans.append(d[i][0])

    return ans


nums = [1, 1, 1, 2, 2, 3]
k = 3
print(topKFrequent(nums, k))
