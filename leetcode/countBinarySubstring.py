class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = [1]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                groups[-1] += 1
            else:
                groups.append(1)
        count = 0
        for i in range(len(groups)-1):
            count += min(groups[i], groups[i+1])
        return count