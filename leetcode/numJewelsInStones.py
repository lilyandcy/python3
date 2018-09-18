class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for char in J:
            if char in S:
                count = count + S.count(char)
        return count