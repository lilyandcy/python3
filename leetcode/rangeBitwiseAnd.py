class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        a = bin(m)[2:]
        b = bin(n)[2:]
        if len(a) != len(b):
            return 0
        i = 0
        length = len(a)
        while i < length and a[i] == b[i]:
            i += 1
        n >>= (length - i)
        n <<= (length - i)
        return n