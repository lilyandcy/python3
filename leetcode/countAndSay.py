class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        if n == 1:
            return res
        for i in range(2, n+1):
            temp = ""
            count = 1
            for j in range(len(res)-1):
                 if res[j] != res[j+1]:
                        temp += str(count) + res[j]
                        count = 1
                 else:
                    count = count + 1
            temp += str(count) + res[-1]
            res = temp
        return res