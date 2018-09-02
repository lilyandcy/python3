class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # handle some corner case first
        if strs.count("") > 0 or strs == []:
            return ('')
        if len(strs) == 1:
            return(strs[0])
        # find the shortest str in strs
        min = len(strs[0])
        for string in strs:
            if len(string) < min:
                min = len(string)
        retstr = ''
        for i in range(min):
            newlist = []
            for string in strs:
                    newlist.append(string[i])
            if newlist.count(newlist[0]) == len(newlist):
                retstr = retstr + string[i]
            else:
                break
        return retstr