# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        addlist = []
        while head.next != None:
            if hash(head) not in addlist:
                addlist.append(hash(head))
            else:
                return True
            head = head.next
        return False