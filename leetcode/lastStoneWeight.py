class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        while len(stones) > 1:
            stone1 = max(stones)
            idxMax1 = stones.index(stone1)
            stones.pop(idxMax1)
            stone2 = max(stones)
            idxMax2 = stones.index(stone2)
            stones.pop(idxMax2)
            if stone1 != stone2:
                newStone = stone1 - stone2
                stones.append(newStone)
        if stones == []:
            return 0
        else:
            return stones[0]