# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# TC: O(N * 4)
# SC: O(N * 5)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 5 for _ in range(n + 1)]
        
        for transaction in range(5): dp[n][transaction] = 0
        for i in range(n + 1): dp[i][0] = 0
        
        for i in range(n - 1, -1, -1):
            for transaction in range(1, 5):
                if transaction % 2 == 0:   # buy allowed
                    dp[i][transaction] = max(-prices[i] + dp[i + 1][transaction - 1],
                                              dp[i + 1][transaction])
                else:                       # sell allowed
                    dp[i][transaction] = max(prices[i] + dp[i + 1][transaction - 1],
                                              dp[i + 1][transaction])
        
        return dp[0][4]
    