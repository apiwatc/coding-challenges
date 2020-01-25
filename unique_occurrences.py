"""
Given an array of integers arr,
write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
"""


def uniqueOccurrences(arr):
    occurrence = {}
    for num in set(arr):
        occurrence[num] = arr.count(num)
    unique = set(occurrence.values())
    return len(occurrence) == len(unique)


arr = [1, 2, 2, 1, 1, 3]
print(uniqueOccurrences(arr))
