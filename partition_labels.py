"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible 
so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""


def partitionLabels(S):
    last = 0
    start = 0
    partition = []
    for i in range(len(S)):
        r = S.rfind(S[i])
        if r > last:
            last = r
        if i >= last:
            partition.append(len(S[start:last+1]))
            start = last + 1

    return partition


S = "ababcbacadefegdehijhklij"
print(partitionLabels(S))
