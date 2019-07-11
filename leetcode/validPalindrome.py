class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            left = s[i+1:j+1]
            right = s[i:j]
            return (left == left[::-1]) or (right == right[::-1])
        return True