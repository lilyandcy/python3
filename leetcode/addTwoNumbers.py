# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return l1
        if l1 == None and l2 != None:
            return l2
        if l1 != None and l2 == None:
            return l1
        s1 = ""
        s2 = ""
        while l1 != None:
            s1 = str(l1.val) + s1
            l1 = l1.next
        while l2 != None:
            s2 = str(l2.val) + s2
            l2 = l2.next
        s3 = str(int(s1) + int(s2))
        start = ListNode(0)
        root = start
        count = 0
        for c in s3[::-1]:
            start.val = int(c)
            count += 1
            if count < len(s3):
                start.next = ListNode(0)
                start = start.next
        return root