"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


def preorderTraversal(self, root: TreeNode) -> List[int]:
    stack = [root]
    ans = []

    while stack:
        node = stack.pop()
        # check node first prvents getting val from NoneType
        if node is not None:
            ans.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return ans
