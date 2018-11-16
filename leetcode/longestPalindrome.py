class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 1
        dictS = {}
        for c in s:
            if dictS.get(c) == None:
                dictS[c] = 1
            else:
                dictS[c] += 1
        odd = False
        length = len(s)
        for key in dictS:
            if dictS[key] % 2 != 0: # value is odd
                length -= 1
                odd = True
        if odd == False:
            return length
        else:
            return length + 1