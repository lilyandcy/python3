class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        rlist = []
        for num in range(left, right + 1):
            strnum = str(num)
            templist = []
            for i in range(len(strnum)):
                templist.append(int(strnum[i]))
            setnum = set(templist)

            status = 0
            for div in setnum:
                if div == 0:
                    status = 0
                    break
                else:
                    if num % div != 0:
                        status = 0
                        break
                    else:
                        status = 1
            if status == 1:
                rlist.append(num)
        return rlist