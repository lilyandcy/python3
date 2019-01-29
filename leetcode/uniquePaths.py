class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        # C(m+n-2, n-1) = (m+n-2)!/(n-1)!(m-1)!
        def factorial(x):
            res = 1
            while x > 0:
                res *= x
                x = x - 1
            return res
        return factorial(m+n-2) // (factorial(n-1)*factorial(m-1))