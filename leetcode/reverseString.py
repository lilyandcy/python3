class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = ""
        i = len(s) - 1
        while i >= 0:
            rs = rs + s[i]
            i = i - 1
        return rs