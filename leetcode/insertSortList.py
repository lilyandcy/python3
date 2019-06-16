# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = ListNode(head.val)
        p1 = dummy.next
        head = head.next
        while head is not None:
            p = dummy
            val = head.val
            node = ListNode(val)
            if p1.val <= val:
                p1.next = node
                p1 = p1.next
            else:
                while p.next.val < val:
                    p = p.next
                node.next = p.next
                p.next = node
            head = head.next
        return dummy.next
