# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# TC: O(N * 2 * 3)
# SC: O(N * 2 * 3)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        
        # Base case: when i = n
        for j in range(2):
            for transaction in range(2):
                dp[n][j][transaction] = 0
        
        # Base case: when transactions = 0
        for i in range(n):
            for buy_allowed in range(2):
                dp[i][buy_allowed][0]
                
        for i in range(n - 1, -1, -1):
            for buy_allowed in range(2):
                for transaction in range(1, 3):
                    if buy_allowed == 1:
                        dp[i][buy_allowed][transaction] = max(-prices[i] + dp[i + 1][0][transaction],
                                                              dp[i + 1][1][transaction])
                    else:
                        dp[i][buy_allowed][transaction] = max(prices[i] + dp[i + 1][1][transaction - 1],
                                                              dp[i + 1][0][transaction])
        return dp[0][1][2]
    