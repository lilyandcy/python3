class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numDict = {'2':['a','b','c'], \
                   '3':['d','e','f'], \
                   '4':['g','h','i'], \
                   '5':['j','k','l'], \
                   '6':['m','n','o'], \
                   '7':['p','q','r','s'], \
                   '8':['t','u','v'], \
                   '9':['w','x','y','z']}
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return numDict[digits]
        else:
            return [x + y for x in numDict[digits[0]] for y in self.letterCombinations(digits[1:])]