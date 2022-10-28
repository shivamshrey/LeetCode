# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n + 1)]
        dp[n][0] = dp[n][1] = 0
        for i in range(n - 1, -1, -1):
            for buy_allowed in range(2):
                profit = 0

                if buy_allowed == 1:
                    profit = max(-prices[i] + dp[i + 1][0],    # buy
                                 dp[i + 1][1])                    # don't buy
                else:
                    profit = max(prices[i] + dp[i + 1][1],        # sell
                                 dp[i + 1][0])                # don't sell

                dp[i][buy_allowed] = profit

        return dp[0][1]
    