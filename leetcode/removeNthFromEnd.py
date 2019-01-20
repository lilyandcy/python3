# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head
        arr = []
        while cur != None:
            arr.append(cur.val)
            cur = cur.next
        arr.pop(-n)
        head = head.next
        cur = head
        for i in range(len(arr)):
            cur.val = arr[i]
            cur = cur.next
        return head