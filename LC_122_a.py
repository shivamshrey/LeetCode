# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(i, buy_allowed):
            if i == n: return 0

            if dp[i][buy_allowed] != -1: return dp[i][buy_allowed]

            profit = 0

            if buy_allowed == 1:
                profit = max(-prices[i] + helper(i + 1, 0),    # buy
                             helper(i + 1, 1))                    # don't buy
            else:
                profit = max(prices[i] + helper(i + 1, 1),        # sell
                             helper(i + 1, 0))                # don't sell

            dp[i][buy_allowed] = profit

            return profit

        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        return helper(0, 1)
    