# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []
        if len(lists) == 1:
            return lists[0]
        if lists.count(None) == len(lists):
            return []
        arr = []
        for ln in lists:
            while ln != None:
                arr.append(ln.val)
                ln = ln.next
        arr.sort()
        res = ListNode(0)
        root = res
        for i in range(len(arr)):
            res.val = arr[i]
            if i != len(arr) - 1:
                res.next = ListNode(0)
                res = res.next
        return root