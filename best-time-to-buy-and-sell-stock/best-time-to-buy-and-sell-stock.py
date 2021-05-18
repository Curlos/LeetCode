class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        maxPrice = 0
        
        for i in range(len(prices) - 1, -1, -1):
            price = prices[i]
            maxProfit = max(maxProfit, maxPrice - price)
            maxPrice = max(maxPrice, price)
        
        return maxProfit