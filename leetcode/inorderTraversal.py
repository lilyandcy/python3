# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res
        if root.left != None:
            res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        if root.right != None:
            res.extend(self.inorderTraversal(root.right))
        return res