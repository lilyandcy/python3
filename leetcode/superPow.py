class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        sum = 0
        for i in b:
            sum = sum * 10 + i
        return pow(a, sum, 1337)