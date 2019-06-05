class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        save = set()
        res = ""
        for word in words:
            if word[:-1] in save or word[:-1] == '':
                if len(word) > len(res):
                    res = word
                save.add(word)
        return res