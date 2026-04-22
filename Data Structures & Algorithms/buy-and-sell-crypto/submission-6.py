class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        low = prices[0]
        most_profit = 0
        while j < len(prices):
            most_profit = max(most_profit, prices[j]-prices[i])
            print(most_profit)
            if prices[j] < low:
                low = prices[j]
                i = j
                j += 1
            else:
                j += 1
        if most_profit < 0:
            return 0
        return most_profit
                
            