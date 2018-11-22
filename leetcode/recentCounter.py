class RecentCounter:

    def __init__(self):
        self.inScope = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if t == None:
            return None
        elif t <= 3001:
            self.inScope.append(t)
            return len(self.inScope)
        else:
            mint = t - 3000
            if self.inScope == [] or self.inScope[-1] < mint:
                self.inScope = [t]
                return 1
            else:
                length = len(self.inScope)
                for i in range(length):
                    if self.inScope[i] >= mint:
                        self.inScope = self.inScope[i:]
                        self.inScope.append(t)
                        return len(self.inScope)




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)