class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        sbinn = bin(n)[2:]
        if len(sbinn) < 32:
            x = 32 - len(sbinn)
            for i in range(x):
                sbinn = "0" + sbinn
        return int(sbinn[::-1], 2)