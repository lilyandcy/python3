class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        r = 1
        while candies > 0:
            for i in range(num_people):
                if candies < 0:
                    break
                if candies > i+1+(r-1)*num_people:
                    ans[i] += (i+1) + (r-1)*num_people
                    candies -= (i+1) + (r-1)*num_people
                else:
                    ans[i] += candies
                    candies = 0
            r += 1
        return ans