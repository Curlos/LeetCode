class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxNum = 0
        maxProfit = 0
        
        for i in range(len(prices) - 1, -1, -1):
            if maxNum - prices[i] > maxProfit:
                maxProfit = maxNum - prices[i]
            if prices[i] > maxNum:
                maxNum = prices[i]
        
        return maxProfit