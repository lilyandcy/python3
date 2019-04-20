class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sumA = sum(A) / 3
        if sumA % 1 != 0:
            return False
        sumTemp = 0
        subCount = 0
        for i in range(len(A)):
            sumTemp += A[i]
            if sumTemp == sumA:
                sumTemp = 0
                subCount += 1
                if subCount == 2:
                    return True
        return False