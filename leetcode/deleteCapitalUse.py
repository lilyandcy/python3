class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower() or word.isupper():
            return True
        for i in range(1, len(word)):
            if word[i].isupper():
                return False
        return True