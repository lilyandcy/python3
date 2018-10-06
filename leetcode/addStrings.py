class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carryStatus = False
        res = ""
        count = min(len(num1), len(num2))
        rnum1 = num1[::-1]
        rnum2 = num2[::-1]
        for i in range(count):
            intResult = int(rnum1[i]) + int(rnum2[i])
            if carryStatus == False:
                if intResult < 10:
                    res = str(intResult) + res
                else:
                    res = str(intResult)[1] + res
                    carryStatus = True
            else:
                if intResult + 1 < 10:
                    res = str(intResult + 1) + res
                    carryStatus = False
                else:
                    res = str(intResult + 1)[1] + res
        if carryStatus == False:
            if len(num1) > len(num2):
                res = num1[:len(num1) - count] + res
            elif len(num2) > len(num1):
                res = num2[:len(num2) - count] + res
        else:
            if len(num1) > len(num2):
                # num1[:len(num1) - count] + 1
                prefix = str(int(num1[:len(num1)-count]) + 1)
                res = prefix + res
            elif len(num2) > len(num1):
                # num2[:len(num2) - count] + 1
                prefix = str(int(num2[:len(num2)-count]) + 1)
                res = prefix + res
            else:
                res = "1" + res
        return res