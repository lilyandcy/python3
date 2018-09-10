class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if (s[i].isdigit() or s[i].isalpha()) and (s[j].isdigit() or s[j].isalpha()):
                if s[i].upper() != s[j].upper():
                    return False
                else:
                    i = i + 1
                    j = j - 1
            else:
                if not(s[i].isdigit() or s[i].isalpha()):
                    i = i + 1
                if not(s[j].isdigit() or s[j].isalpha()):
                    j = j - 1
        return True