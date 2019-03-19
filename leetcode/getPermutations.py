import itertools
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        count = 1
        for i in range(n):
            nums.append(i+1)
        for i in itertools.permutations(nums,n):
            num = ""
            for j in i:
                num += str(j)
            if count == k:
                return num
            count += 1