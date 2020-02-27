"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


def multiply(num1, num2):
    num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
           '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    first = 0
    second = 0
    for n in num1:
        first = (first * 10) + num[n]
    for n in num2:
        second = (second * 10) + num[n]

    return str((first * second))


num1 = '123'
num2 = '456'
print(multiply(num1, num2))
