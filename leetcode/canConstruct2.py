class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        clist = set(list(ransomNote))
        for char in clist:
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True