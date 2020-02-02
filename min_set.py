"""
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Example 1:
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
"""


def minSetSize(arr):
    count = {}
    for num in arr:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

    removes = 0
    size = 0
    for (k, v) in sorted(count.items(), key=lambda kv: kv[1], reverse=True):
        # removes = most duplicate numbers add up
        # if >= half, then return size of set of duplicate numbers
        removes += v
        size += 1
        if removes >= len(arr)//2:
            return size


arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
print(minSetSize(arr))
