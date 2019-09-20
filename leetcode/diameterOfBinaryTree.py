# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_d = 0
        self.treeview(root)
        return self.max_d

    def treeview(self, root):
        if root is None:
            return 0
        left_length = self.treeview(root.left)
        right_length = self.treeview(root.right)
        if left_length + right_length > self.max_d:
            self.max_d = left_length + right_length
        return max(left_length+1, right_length+1)