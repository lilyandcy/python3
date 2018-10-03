"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        rlist = []
        if root == None:
            return rlist
        rlist.append(root.val)
        for i in range(len(root.children)):
            rlist.extend(self.preorder(root.children[i]))
        return rlist