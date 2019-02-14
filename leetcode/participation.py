# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        tempList = []
        cur = head
        while cur != None:
            tempList.append(cur.val)
            cur = cur.next
        if x > max(tempList) or x < min(tempList):
            return head
        arr = [x]
        indexX = 0
        for i in range(len(tempList)):
            if tempList[i] < x:
                arr.insert(indexX, tempList[i])
                indexX += 1
            else:
                arr.append(tempList[i])
        arr.pop(indexX)
        cur = head
        i = 0
        while cur != None:
            cur.val = arr[i]
            cur = cur.next
            i += 1
        return head