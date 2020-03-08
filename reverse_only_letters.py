"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
"""


def reverseOnlyLetters(S):
    s = list(S)
    l = 0
    r = len(s)-1
    while l < r:
        if s[l].isalpha() and s[r].isalpha():
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        if not s[l].isalpha():
            l += 1
        if not s[r].isalpha():
            r -= 1
    return ''.join(s)


S = "a-bC-dEf-ghIj"
print(reverseOnlyLetters(S))
