# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        if not root:
            return []
        res = []
        temp = []

        def getPath(node, nowSum):
            if not node:
                return
            nowSum += node.val
            temp.append(node.val)
            if not node.left and not node.right and nowSum == sum:
                res.append(temp.copy())
                temp.pop()
                return
            getPath(node.left, nowSum)
            getPath(node.right, nowSum)
            temp.pop()

        getPath(root,0)
        return res