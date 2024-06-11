from typing import List
# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


# The first time
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        start, end = 0, 1
        max_profit = 0
        current_profit = 0

        while end < len(prices):
            buy = prices[start]
            sell = prices[end]
            current_profit = sell - buy
            if current_profit > 0: # profitable?
                # if current_profit >= max_profit:
                #     max_profit = current_profit
                max_profit = max(max_profit, current_profit)
            else:
                start = end
            end += 1
        
        return max_profit
    
# The second time
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low, sell high
        left, right = 0, 1 # left: buy, right: sell, must buy before sell
        max_diff = 0
        while right < len(prices):
            diff = prices[right] - prices[left]
            if diff >= 0: # profitable
                max_diff = max(max_diff, diff)
                right += 1
            else:
                left += 1
                
        return max_diff if max_diff > 0 else 0
        # Idea: Not profitable, then move left 1 position, meaning to BUY the stock in the next day. If profitable, then move right to 1 position, meaning to SELL the stock in the next day until it is not profitable

