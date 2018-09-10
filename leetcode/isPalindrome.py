class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        slist = []
        news = s.upper()
        for c in news:
            if c.isdigit() or c.isalpha():
                slist.append(c)
        rslist = slist.copy()
        rslist.reverse()
        if rslist == slist:
            return True
        else:
            return False