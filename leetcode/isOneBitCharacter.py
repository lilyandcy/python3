class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        length = len(bits)
        i = 0
        while i < length - 1:
            if bits[i] == 1:
                i += 1
                if i == length - 1:
                    return False
            i += 1
        return True