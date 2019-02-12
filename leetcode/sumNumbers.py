# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = 0
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left:
            root.left.val += 10*root.val
        if root.right:
            root.right.val += 10*root.val
        if root.left == None and root.right == None:
            self.res += root.val
        self.sumNumbers(root.left)
        self.sumNumbers(root.right)
        return self.res