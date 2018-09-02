class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        originalNum = 0
        for i in range(len(digits)):
            j = len(digits) - i
            originalNum = originalNum + digits[i] * (10 ** (j-1))
        nNum = originalNum + 1
        newdigits = []
        while nNum > 0:
            newdigits.append(nNum%10)
            nNum = nNum // 10
        rdigits = []
        i = len(newdigits)
        while i > 0:
            rdigits.append(newdigits[i-1])
            i = i - 1
        return rdigits