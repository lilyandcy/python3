class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return 2**(len(bin(N))-2) - 1 - N