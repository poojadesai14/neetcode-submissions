class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] 
        profit = 0

        for i in range(1, len(prices)):
            cost = prices[i]-min_price
            profit = max(profit, cost)
            min_price = min(min_price,prices[i])
        
        return profit


        