class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        Num = []
        n = len(p)
        A = [0] * 26
        for i in range(n):
            A[ord(p[i]) - ord('a')] += 1
            A[ord(s[i]) - ord('a')] -= 1
        if A == [0] * 26:
            Num.append(0)
        for i in range(n, len(s)):
            A[ord(s[i]) - ord('a')] -= 1
            A[ord(s[i-n]) - ord('a')] += 1
            if A == [0] * 26:
                Num.append(i + 1 - n)
        return Num