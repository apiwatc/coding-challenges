"""
Given a string s formed by digits ('0' - '9') and '#' .
We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

Example 1:
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
"""


def freqAlphabets(s):
    ans = []
    i = len(s)-1
    while i >= 0:
        # j = 106 = 10#  so 96 + s[i]
        if s[i] == '#':
            c = s[i-2:i]
            i -= 3
            ans.append(chr(96 + int(c)))
        else:
            ans.append(chr(96 + int(s[i])))
            i -= 1

    return ''.join(ans[::-1])


s = "10#11#12"
print(freqAlphabets(s))
