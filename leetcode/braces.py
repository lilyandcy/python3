class Solution:
    def braces(self, stringList):
        """
        :List stringList:
        :rtype List
        """
        dictBraces = {"}":"{", "]":"[", ")":"("}
        res = []
        for strings in stringList:
            stackString = []
            for i in range(len(strings)):
                if dictBraces.has_key(strings[i]) == False:
                    stackString.append(strings[i])
                else:
                    if dictBraces[strings[i]] != stackString.pop():
                        res.append("NO")
                        break
            if len(stackString) != 0:
                res.append("NO")
            else:
                res.append("YES")
        return res
