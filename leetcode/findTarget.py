class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        tempList = self.preOrder(root)
        for i in range(len(tempList)):
            target = k - tempList[i]
            if target == tempList[i]:
                if tempList.count(target) > 1:
                    return True
            else:
                if target in tempList:
                    return True
        return False

    def preOrder(self, root):
        res = []
        if root == None:
            return res
        res.append(root.val)
        res.extend(self.preOrder(root.left))
        res.extend(self.preOrder(root.right))
        return res
