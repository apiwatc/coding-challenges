"""
Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
1 -> 0 -> 1 
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getDecimalValue(self, head):
    str_num = ''
    temp = head
    while temp:
        str_num += str(temp.val)
        temp = temp.next
    return int(str_num, 2)  # convert string numbers to binary using int()
