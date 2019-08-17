class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        count = 0
        maxd = 0
        maxd2 = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                maxd2 += 1
            else:
                break
        for i in seats:
            if i == 0:
                count += 1
            else:
                if int((count+1)/2) > maxd:
                    maxd = int((count+1)/2)
                count = 0
        return max(maxd, maxd2, count)