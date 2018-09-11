class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sets = set(s)
        # all chars in s are the same.
        if len(s) == 1:
            return False
        if len(sets) == 1:
            return True
        sublen = 2
        while sublen <= len(s)//2:
            if len(s) % sublen != 0:
                sublen = sublen + 1
            else:
                count = len(s) // sublen
                i = 0
                for j in range(count):
                    if s[i:i+sublen] != s[:sublen]:
                        sublen = sublen + 1
                        break
                    else:
                        i = i + sublen
                        if i >= len(s):
                            return True
        return False