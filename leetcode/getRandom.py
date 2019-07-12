# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.collect = []
        while head:
            self.collect.append(head.val)
            head = head.next
        self.length = len(self.collect) - 1

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return self.collect[random.randint(0, self.length)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()