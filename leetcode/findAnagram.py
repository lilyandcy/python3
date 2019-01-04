class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        slen = len(s)
        plen = len(p)
        if slen < plen:
            return res
        pf = [0] * 26
        for i in range(plen):
            pf[ord(p[i]) - 97] += 1
        for i in range(slen - plen + 1):
            sf = [0] * 26
            for j in range(i, i+plen):
                sf[ord(s[j]) - 97] += 1
            if sf == pf:
                res.append(i)
        return res