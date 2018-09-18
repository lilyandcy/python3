class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slist = []
        tlist = []
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            slist.append(s[i])
        for i in range(len(t)):
            tlist.append(t[i])
        slist.sort()
        tlist.sort()
        if slist != tlist:
            return False
        else:
            return True