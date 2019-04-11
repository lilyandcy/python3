class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        fibList = [0] * (N+1)
        fibList[1] = 1
        for i in range(2, N+1):
            fibList[i] = fibList[i-1] + fibList[i-2]
        return fibList[-1]