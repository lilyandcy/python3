class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = len(S)
        res = []
        low = 0
        high = N
        count = 0
        while count < N:
            if S[count] == "I":
                res.append(low)
                low += 1
            if S[count] == "D":
                res.append(high)
                high -= 1
            count += 1
        res.append(low)
        return res