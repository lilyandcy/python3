class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vset = {"a","e","i","o","u","A","E","I","O","U"}
        slist = list(s)
        temp = ""
        i = 0
        j = len(slist) - 1
        while i < j:
            if (slist[i] in vset) and (slist[j] in vset):
                temp = slist[i]
                slist[i] = slist[j]
                slist[j] = temp
                i = i + 1
                j = j - 1
            else:
                if slist[i] not in vset:
                    i = i + 1
                if slist[j] not in vset:
                    j = j - 1
        return "".join(slist)