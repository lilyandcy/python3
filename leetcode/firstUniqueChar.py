class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cset = set(list(s))
        location = len(s) - 1
        found = False
        for char in cset:
            if s.count(char) == 1:
                found = True
                if s.find(char) < location:
                    location = s.find(char)

        if found == False:
            return -1
        return location