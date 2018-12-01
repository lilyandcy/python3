# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.getLeafList(root1) == self.getLeafList(root2)

    def getLeafList(self, root):
        """
        :type root: TreeNode
        :rtype: list[int]
        """
        res = []
        if root == None:
            return res
        if root.left == None and root.right == None:
            res.append(root.val)
            return res
        else:
            if root.left!= None:
                res.extend(self.getLeafList(root.left))
            if root.right!= None:
                res.extend(self.getLeafList(root.right))
        return res
