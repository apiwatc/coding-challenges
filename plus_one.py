"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""


def plusOne(digits):
    num_to_str = ''
    num_plus_one = []
    # turn number to strings
    for i in digits:
        num_to_str += str(i)
    # plus one to number
    plus_one = int(num_to_str) + 1
    # append each digit from list strings number to new int list
    for i in str(plus_one):
        num_plus_one.append(int(i))
    return num_plus_one


digits = [1, 2, 3]
print(plusOne(digits))
