"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
"""
import collections


def isAnagram(s, t):
    return collections.Counter(s) == collections.Counter(t)


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
