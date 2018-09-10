class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist = s.split(" ")
        i = len(slist) - 1
        while i >= 0:
            if slist[i] != "":
                return len(slist[i])
            else:
                i = i - 1
        return 0