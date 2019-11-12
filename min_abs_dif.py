"""
Given an array of distinct integers arr,
find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
   - a, b are from arr
   - a < b
   - b - a equals to the minimum absolute difference of any two elements in arr

Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
"""


def minimumAbsDifference(arr):
    min_abs_dif = []
    arr.sort()

    # pair each element from two equal-length lists
    dif = min(j-i for i, j in zip(arr, arr[1:]))
    for i in range(len(arr)-1):
        for j in range(1):
            if arr[i+1] - arr[i] == dif:
                min_abs_dif.append([arr[i], arr[i+1]])

    return min_abs_dif


arr = [3, 8, -10, 23, 19, -4, -14, 27]
print(minimumAbsDifference(arr))
