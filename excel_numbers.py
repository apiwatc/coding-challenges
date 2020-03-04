"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:
Input: "ZY"
Output: 701
"""


def titleToNumber(s):
    ans = 0
    for c in s:
        ans = (ans * 26) + ord(c)-64

    return ans


s = "AAA"
print(titleToNumber(s))
