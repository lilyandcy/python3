class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s, res, cul = 0, 0, {}
        cul[0] = 1
        for i in range(len(nums)):
            s += nums[i]
            if s - k in cul:
                res += cul[s-k]
            if s not in cul:
                cul[s] = 0
            cul[s] += 1
        return res