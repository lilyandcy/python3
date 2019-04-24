class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        index = 0
        res = False
        for i in range(len(t)):
            if s[index] == t[i]:
                index += 1
            if index == len(s):
                res = True
                break
        return res