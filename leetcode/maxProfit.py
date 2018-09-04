class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if prices == []:
            return profit
        minPrice = prices[0]
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif profit < prices[i] - minPrice:
                profit = prices[i] - minPrice
        return profit
