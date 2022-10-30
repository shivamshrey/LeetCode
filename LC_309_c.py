# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 2)]
        dp[n][0] = dp[n][1] = 0 # optional as all values are 0
        
        for i in range(n - 1, -1, -1):              
            dp[i][1] = max(-prices[i] + dp[i + 1][0],    # buy
                           dp[i + 1][1])                    # don't buy

            dp[i][0] = max(prices[i] + dp[i + 2][1],        # sell
                           dp[i + 1][0])                # don't sell

        return dp[0][1]
    