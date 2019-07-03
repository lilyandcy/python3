class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortHeights = copy.deepcopy(heights)
        sortHeights.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i] != sortHeights[i]:
                count += 1
        return count