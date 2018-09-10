class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        clist = []
        for char in ransomNote:
            if char not in clist:
                clist.append(char)
                if ransomNote.count(char) > magazine.count(char):
                    return False
            else:
                continue
        return True