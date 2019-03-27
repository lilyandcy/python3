class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = {}
        for x in nums:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
        return [x for x in dic.keys() if dic[x] > n/3]