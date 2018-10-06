"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        rlist = []
        if root == None:
            return rlist
        for child in root.children:
            rlist.extend(self.postorder(child))
        rlist.append(root.val)
        return rlist