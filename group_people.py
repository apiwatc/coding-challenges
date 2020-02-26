"""
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. 
Given the array groupSizes of length n telling the group size each person belongs to, 
return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. 
Also, it is guaranteed that there exists at least one solution. 

 
Example 1:
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
"""


def groupThePeople(groupSizes):
    ids = {}
    ans = []
    # put same w/ same groupSize into same bucket
    for id, size in enumerate(groupSizes):
        ids.setdefault(size, []).append(id)
    # seperate them into small groups based on size
    for k, v in ids.items():
        for i in range(0, len(v), k):
            ans.append(v[i:i+k])

    return ans


groupSizes = [3, 3, 3, 3, 3, 1, 3]
print(groupThePeople(groupSizes))
