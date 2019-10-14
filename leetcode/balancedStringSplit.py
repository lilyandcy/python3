class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        countL = 0
        for i in range(len(s)):
            if s[i] == 'L':
                countL += 1
            else:
                countL -= 1
            if countL == 0:
                res += 1
        return res