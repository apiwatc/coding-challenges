"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""


def replaceElements(arr):
    last = -1
    for i in range(len(arr)-1, -1, -1):
        arr[i], last = last, max(arr[i], last)
    return arr


arr = [17, 18, 5, 4, 6, 1]
print(replaceElements(arr))
