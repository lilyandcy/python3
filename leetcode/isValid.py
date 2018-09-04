class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        if len(s) % 2 != 0:
            return False
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False

        tempStack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                tempStack.append(c)
            else:
                if c == ")" and tempStack[len(tempStack) - 1] != "(":
                    return False
                if c == "]" and tempStack[len(tempStack) - 1] != "[":
                    return False
                if c == "}" and tempStack[len(tempStack) - 1] != "{":
                    return False
                else:
                    tempStack.pop()
        if len(tempStack) != 0:
            return False
        return True