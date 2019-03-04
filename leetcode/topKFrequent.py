class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapNum = {}
        for num in nums:
            if num in mapNum.keys():
                mapNum[num] += 1
            else:
                mapNum[num] = 1
        listMapNum = sorted(mapNum.items(), key = lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(listMapNum[i][0])
        return res