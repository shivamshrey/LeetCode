# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# TC: O(N)
# SC: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0
        
        for i in range(len(prices)):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i] -  buy1)
            buy2 = min(buy2, prices[i] - sell1)
            sell2 = max(sell2, prices[i] - buy2)
        
        return sell2
    