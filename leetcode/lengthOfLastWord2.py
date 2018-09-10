class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Optimized way to set two pointers.
        # One points to the first non blank char from the tail.
        # Another points to the first blank char before first non blank char
        startindex = len(s) - 1
        endindex = 0
        # Find the location of first non blank char
        i = len(s) - 1
        while i >= 0:
            if s[i] == " ":
                startindex = i - 1
            else:
                break
            i = i - 1
        # judge if the string is with all blank chars
        if startindex < 0:
            return 0
        # Find the location of first blank char before the non blank char
        while i >= 0:
            if s[i] == " ":
                endindex = i
                break
            else:
                i = i - 1
                endindex = i
        # Return distance
        return startindex - endindex