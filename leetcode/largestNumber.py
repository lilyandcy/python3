from functools import cmp_to_key
class Solution:
    def cmp(self, num1, num2):
        str1 = str(num1)
        str2 = str(num2)
        if str1+str2 > str2+str1:
            return -1
        else:
            return 1

    def largestNumber(self, nums: List[int]) -> str:
        num = sorted(nums, key = cmp_to_key(self.cmp))
        if num[0] == 0:
            return "0"
        return "".join(str(i) for i in num)