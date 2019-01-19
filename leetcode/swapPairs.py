# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        cur = head
        arr = []
        while cur != None:
            arr.append(cur.val)
            cur = cur.next
        arrL = len(arr)
        if arrL % 2 == 0:
            for i in range(0, arrL, 2):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        else:
            for i in range(0, arrL-1, 2):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        cur = head
        i = 0
        while cur != None:
            cur.val = arr[i]
            i += 1
            cur = cur.next
        return head