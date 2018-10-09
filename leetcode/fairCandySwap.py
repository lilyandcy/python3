class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        sumB = sum(B)
        setB = set(B)
        target = (sumA + sumB) // 2
        for a in A:
            b = target - (sumA - a)
            if b in setB:
                return [a, b]