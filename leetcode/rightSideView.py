# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        tem = []
        res = []
        depth = 1
        if root:
            tem.append((root, depth))
        else:
            return res
        while len(tem) >= 1:
            top = tem[0][0]
            depth = tem[0][1]
            if top.left:
                tem.append((top.left, depth + 1))
            if top.right:
                tem.append((top.right, depth + 1))
            tem.pop(0)
            if len(tem) > 0 and depth != tem[0][1]:
                res.append(top.val)
        if len(res) == 0 or depth != len(res):
            res.append(top.val)
        return res