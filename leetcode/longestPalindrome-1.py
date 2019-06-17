class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        if self.is_Palindrome(s):
            return s
        for i in range(len(s)-1, 1, -1):
            for j in range(len(s)-i):
                if self.is_Palindrome(s[j:j+i]):
                    return s[j:j+i]
        return s[0]

    def is_Palindrome(self, s):
        return s == s[::-1]