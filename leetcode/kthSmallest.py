# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def preTraversal(self, node):
            res = []
            if node == None:
                return res
            res.append(node.val)
            if node.left:
                res.extend(preTraversal(self, node.left))
            if node.right:
                res.extend(preTraversal(self, node.right))
            return res
        temp = preTraversal(self, root)
        temp.sort()
        return temp[k-1]