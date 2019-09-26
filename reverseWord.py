# Given an input string, reverse the string word by word.

""" 1. A word is defined as a sequence of non-space characters.
    2. Input string may contain leading or trailing spaces. However, 
        your reversed string should not contain leading or trailing spaces.
    3. You need to reduce multiple spaces between two words to a single space 
        in the reversed string.

    Input: "  hello world!  "
    Output: "world! hello"
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return ' '.join(reversed(s))


rev = Solution()
print(rev.reverseWords('the sky is blue'))
