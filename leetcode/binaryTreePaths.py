# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        res = []
        stack = [(root, "")]
        while stack:
            node, ls = stack.pop()
            if node.left == None and node.right == None:
                res.append(ls + str(node.val))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
        return res