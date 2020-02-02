"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true
"""

import re


def isPalindrome(s):
    s = re.sub('[^a-zA-Z0-9]', '', s)
    return s.lower() == s[::-1].lower()


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
