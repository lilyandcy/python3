# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            fast = head.next.next
            slow = head.next
        else:
            return None
        while fast:
            if fast != slow:
                if fast.next:
                    fast = fast.next.next
                else:
                    return None
                slow = slow.next
            else:
                detection = head
                while detection != slow:
                    slow = slow.next
                    detection = detection.next
                return detection