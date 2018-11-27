class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        for num in range(L, R+1):
            number = bin(num).count("1")
            if self.isPrime(number):
                res += 1
        return res


    def isPrime(self, n):
        """
        :type n: int
        :rtype: boolean
        """
        if n > 1:
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for current in range(3, int(math.sqrt(n) + 1), 2):
                if n % current == 0:
                    return False
            return True
        return False