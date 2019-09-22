# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def testSub(self, s, t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        if s.val != t.val:
            return False
        return self.testSub(s.left, t.left) and self.testSub(s.right, t.right)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        res = False
        if s != None:
            if s.val == t.val:
                res = self.testSub(s,t)
            if not res:
                res = self.isSubtree(s.right, t)
            if not res:
                res = self.isSubtree(s.left, t)
        return res
