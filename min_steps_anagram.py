"""
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
"""
import collections


def minSteps(s, t):
    dict_s = collections.Counter(s)
    dict_t = collections.Counter(t)
    return sum((dict_t-dict_s).values())


s = "leetcode"
t = "practice"
print(minSteps(s, t))
