class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strList = str.split(" ")
        if len(strList) != len(pattern):
            return False
        dictP = {}
        dictS = {}
        for i in range(len(pattern)):
            if dictP.get(pattern[i]) == None:
                dictP[pattern[i]] = strList[i]
            else:
                if strList[i] != dictP[pattern[i]]:
                    return False
        for i in range(len(strList)):
            if dictS.get(strList[i]) == None:
                dictS[strList[i]] = pattern[i]
            else:
                if pattern[i] != dictS[strList[i]]:
                    return False
        return True