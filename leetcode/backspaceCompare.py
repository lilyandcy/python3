class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stackS = []
        stackT = []
        for char in S:
            if char != "#":
                stackS.append(char)
            else:
                if stackS != []:
                    stackS.pop()
        for char in T:
            if char != "#":
                stackT.append(char)
            else:
                if stackT != []:
                    stackT.pop()
        return stackS == stackT