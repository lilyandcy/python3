class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for char in t:
            if char not in s:
                return char
            else:
                if t.count(char) != s.count(char):
                    return char