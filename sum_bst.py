"""
Given the root node of a binary search tree, 
return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def range_sum_bst(self, root: TreeNode, left, right) -> int:
        sumBST = 0
        if not root:
            return 0
        else:
            if L <= root.val <= R:
                sumBST += root.val
            if root.val > L and root.left:
                sumBST += self.rangeSumBST(root.left, L, R)
            if root.val < R:
                sumBST += self.rangeSumBST(root.right, L, R)

        return sumBST
