class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        newBed = [0] + flowerbed + [0]
        for i in range(1, len(newBed) - 1):
            if newBed[i-1] == 0 and newBed[i] == 0 and newBed[i+1] == 0:
                newBed[i] = 1
                n -= 1
            if n == 0:
                return True
        return False