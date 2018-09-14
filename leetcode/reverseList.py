# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        pre = None
        cur = head
        while cur.next:
            cur.next = pre
            pre = cur
            cur = cur.next
        cur.next = pre
        head = cur
        return head