"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.
"""


def maximum69Number(num):
    # max_num = [num]
    # arr = list(str(num))
    # for i in range(len(arr)):
    #     temp = arr.copy()
    #     if arr[i] == '6':
    #         temp[i] = '9'
    #         max_num.append(int(''.join(temp)))
    # return max(max_num)
    max_num = str(num)
    return int(max_num.replace('6', '9', 1))


num = 9669
print(maximum69Number(num))
