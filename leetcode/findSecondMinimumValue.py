# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left == None and root.right == None:
            return -1
        if root.left.val == root.right.val == root.val:
            if self.findSecondMinimumValue(root.left) != -1 and self.findSecondMinimumValue(root.right) != -1:
                return min(self.findSecondMinimumValue(root.left), self.findSecondMinimumValue(root.right))
            elif self.findSecondMinimumValue(root.left) == -1:
                return self.findSecondMinimumValue(root.right)
            elif self.findSecondMinimumValue(root.right) == -1:
                return self.findSecondMinimumValue(root.left)
            else:
                return -1
        else:
            if min(root.left.val, root.right.val) != root.val:
                return min(root.left.val, root.right.val)
            else:
                if root.left.val > root.right.val:
                    rval = self.findSecondMinimumValue(root.right)
                    if rval == -1:
                        return root.left.val
                    else:
                        return min(root.left.val, rval)
                else:
                    lval = self.findSecondMinimumValue(root.left)
                    if lval == -1:
                        return root.right.val
                    else:
                        return min(root.right.val, lval)