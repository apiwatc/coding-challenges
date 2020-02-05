"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true
"""


def isValid(s):
    brackets = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for c in s:
        if c in brackets:
            stack.append(c)
        else:
            if not stack or c != brackets[stack[-1]]:
                return False
            else:
                stack.pop()

    return len(stack) == 0


s = "()({[]}){)"
print(isValid(s))
