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
