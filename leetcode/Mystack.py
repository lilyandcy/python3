class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.topstack = None


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.topstack = x



    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        stacklen = len(self.stack)
        if stacklen == 1:
            self.stack.pop(0)
            return self.topstack
        for i in range(stacklen-1):
            temp = self.stack[0]
            self.stack.pop(0)
            self.stack.append(temp)
        self.topstack = temp
        res = self.stack.pop(0)
        return res



    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.topstack


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.stack



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()