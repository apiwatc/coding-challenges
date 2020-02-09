"""
Given an array of integers arr and two integers k and threshold.

Return the number of sub-arrays of size k and average greater than or equal to threshold.

Example 1:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
"""


def numOfSubarrays(arr, k, threshold):
    count = 0
    window_sub = sum(arr[:k])

    for i in range(len(arr)-k):
        if window_sub // k >= threshold:
            count += 1
        window_sub += arr[i+k]
        window_sub -= arr[i]

    if window_sub // k >= threshold:
        count += 1

    return count


arr = [7, 7, 7, 7, 7, 7, 7]
k = 7
threshold = 7
print(numOfSubarrays(arr, k, threshold))
