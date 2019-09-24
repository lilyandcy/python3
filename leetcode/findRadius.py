class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        houses.sort()
        res = []
        start = 0
        end = len(heaters) - 1
        for house in houses:
            while True:
                if house < heaters[start] and start != 0:
                    res.append(min(abs(heaters[start]-house), abs(house-heaters[start-1])))
                    end = len(heaters) - 1
                    break
                elif house == heaters[start] or house == heaters[end]:
                    res.append(0)
                    break
                elif house > heaters[end] and end != len(heaters) - 1:
                    res.append(min(abs(house-heaters[end]), abs(heaters[end+1]-house)))
                    end = len(heaters) - 1
                    break
                elif house < heaters[0]:
                    res.append(heaters[0]-house)
                    break
                elif house > heaters[len(heaters)-1]:
                    res.append(house-heaters[len(heaters)-1])
                    break
                start += 1
                end -= 1
        return max(res)