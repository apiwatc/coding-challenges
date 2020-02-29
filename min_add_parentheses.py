"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', 
and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:
    It is the empty string, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Example 1:
Input: "())"
Output: 1
"""


def minAddToMakeValid(S):
    stack = []
    for paren in S:
        if paren == '(':
            stack.append(paren)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(paren)

    return len(stack)


S = "()))(("
print(minAddToMakeValid(S))
