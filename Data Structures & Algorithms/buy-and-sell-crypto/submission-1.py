class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        cheapest = prices[0]

        for i in range(1,len(prices)):
            profit = prices[i] - cheapest
            res = max(profit, res)
            cheapest = min(prices[i], cheapest)
        return res

        