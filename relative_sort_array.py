"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct,
and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
"""


def relativeSortArray(arr1, arr2):
    relative = []
    counter = {}
    not_in = []
    arr1.sort()

    for num in arr2:
        counter[num] = 0

    for num in arr1:
        if num in counter:
            counter[num] += 1
        else:
            not_in.append(num)

    for num in arr2:
        relative.extend([num] * counter[num])
    else:
        relative.extend(not_in)

    return relative


arr1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13,
        12, 27, 12, 24, 5, 23, 29, 48, 30, 31]
arr2 = [2, 42, 38, 0, 43, 21]
print(relativeSortArray(arr1, arr2))
