class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wlist = s.split(" ")
        for i in range(len(wlist)):
            wlist[i] = wlist[i][::-1]
        rs = " ".join(wlist)
        return rs