class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        countPrime = 0
        for i in range(1, n+1):
            countPrime += self.isPrime(i)
        countNonPrime = n - countPrime
        res = 1
        for i in range(1, countPrime+1):
            res = res * i % (1000000000 + 7)
        for i in range(1, countNonPrime+1):
            res = res * i % (1000000000 + 7)
        return res

    def isPrime(self, num: int) -> int:
        if 1 < num <= 3:
            return 1
        if num <= 1:
            return 0
        if num % 6 != 1 and num % 6 != 5:
            return 0
        sqrt = int(num ** 0.5)
        for i in range(5, sqrt+1, 6):
            if num % i == 0 or num % (i+2) == 0:
                return 0
        return 1