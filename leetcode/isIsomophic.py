class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictS = {}
        dictT = {}
        for i in range(len(s)):
            if dictS.get(s[i]) == None:
                dictS[s[i]] = t[i]
            else:
                if dictS[s[i]] != t[i]:
                    return False
            if dictT.get(t[i]) == None:
                dictT[t[i]] = s[i]
            else:
                if dictT[t[i]] != s[i]:
                    return False
        return True
