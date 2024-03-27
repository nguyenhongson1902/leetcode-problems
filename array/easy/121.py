from typing import List
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


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