# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodeVals = []
        def dfs(node):
            if node:
                nodeVals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return len(set(nodeVals)) == 1