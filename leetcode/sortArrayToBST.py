# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        if n == 0:
            return None
        mid = n // 2
        nd = TreeNode(nums[mid])
        nd.left = self.sortedArrayToBST(nums[:mid])
        nd.right = self.sortedArrayToBST(nums[mid+1:])
        return nd

    def sortedListToBST(self, head: 'ListNode') -> 'TreeNode':
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        valList = []
        cur = head
        while cur != None:
            valList.append(cur.val)
            cur = cur.next
        return self.sortedArrayToBST(valList)