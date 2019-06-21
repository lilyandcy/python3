class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        if n == 0:
            return [[]]

        for i in range(1, n+1):
            if self.isPalindrome(s[:i]):
                leftpart = [s[:i]]
                if i == n:
                    res.append(leftpart)
                else:
                    rightpart = self.partition(s[i:])
                    for item in rightpart:
                        res.append(leftpart+item)
        return res
    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False