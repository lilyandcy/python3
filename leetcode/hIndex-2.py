class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low, high, l = 0, len(citations) - 1, len(citations)
        res = 0
        while low <= high:
            mid = low + (high - low) // 2
            if citations[mid] >= l - mid:
                res = l - mid
                high = mid - 1
            elif citations[mid] < l - mid:
                low = mid + 1
        return res