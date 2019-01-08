class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        maxb = 10 ** n - 1
        minb = 10 ** (n - 1)
        i = maxb
        while i > minb:
            mix = self.buildPalindrome(i)
            j = maxb
            while j * j >= mix:
                if mix % j == 0 and mix / j <= maxb:
                    return mix % 1337
                j -= 1
            i -= 1
        return -1

    def buildPalindrome(self, x):
        """
        :type x: int
        :rtype: long
        """
        s = str(x)[::-1]
        paNum = int(str(x) + s)
        return paNum