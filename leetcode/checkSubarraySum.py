class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0:-1}
        sumNum = 0
        for i in range(len(nums)):
            sumNum += nums[i]
            if k != 0:
                sumNum = sumNum % k
            if hashmap.get(sumNum) != None:
                if i - hashmap[sumNum] > 1:
                    return True
            else:
                hashmap[sumNum] = i
        return False