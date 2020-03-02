"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

from collections import Counter, OrderedDict


def firstuniqChar(s):
    d = OrderedDict(Counter(s))
    for k, v in d.items():
        if v == 1:
            return s.index(k)
    return -1


s = 'loveleetcode'
print(firstuniqChar(s))
