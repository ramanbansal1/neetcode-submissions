class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        future_max = 0
        i = len(prices) - 1
        while i >= 0:
            future_max = max(future_max, prices[i])
            profit = max(future_max - prices[i], profit)
            i -= 1
        return profit