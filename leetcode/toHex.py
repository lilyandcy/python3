class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        dictDec = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        decnum = ""
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32
        while num > 15:
            decnum = dictDec[num % 16] + decnum
            num = num // 16
        if num != 0:
            decnum = dictDec[num] + decnum
        return decnum