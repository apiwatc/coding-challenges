"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""


def reverseWords(s):
    slist = s.split()
    for i in range(len(slist)):
        slist[i] = slist[i][::-1]
    return ' '.join(slist)


s = "Let's take LeetCode contest"
print(reverseWords(s))
