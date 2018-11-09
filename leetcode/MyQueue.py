class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.head = None


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.queue == []:
            self.head = x
        self.queue.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        length = len(self.queue)
        if length == 1:
            return self.queue.pop()
        else:
            tempq = self.queue[::-1]
            res = tempq.pop()
            self.queue = tempq[::-1]
            self.head = self.queue[0]
            return res


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.head

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.queue



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()