class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        countFive = 0
        countTen = 0
        if len(bills) == 0:
            return True
        for bill in bills:
            if bill == 5:
                countFive += 1
            if bill == 10:
                if countFive != 0:
                    countFive -= 1
                    countTen += 1
                else:
                    return False
            if bill == 20:
                if countTen != 0 and countFive != 0:
                    countTen -= 1
                    countFive -= 1
                elif countFive > 2:
                    countFive -= 3
                else:
                    return False
        return True