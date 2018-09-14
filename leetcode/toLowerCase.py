class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        rstr = ""
        for i in range(len(str)):
            if str[i].isupper():
                rstr = rstr + str[i].lower()
            else:
                rstr = rstr + str[i]
        return rstr