# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = [root]
        res = []
        while queue:
            count = len(queue)
            sum = 0
            for i in range(count):
                node = queue.pop(0)
                sum += node.val
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            res.append(sum/count)
        return res