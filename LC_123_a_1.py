# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# TC: O(N * 2 * 3)
# SC: O(N * 2 * 3) + O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(i, buy_allowed, transactions):
            if i == n or transactions == 0: return 0
            if dp[i][buy_allowed][transactions] != -1: return dp[i][buy_allowed][transactions]
            if buy_allowed == 1:
                dp[i][buy_allowed][transactions] = max(-prices[i] + helper(i + 1, 0, transactions),
                                                       helper(i + 1, 1, transactions))
            else:
                dp[i][buy_allowed][transactions] = max(prices[i] + helper(i + 1, 1, transactions - 1),
                                                       helper(i + 1, 0, transactions))
            return dp[i][buy_allowed][transactions]

        n = len(prices)
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]
        return helper(0, 1, 2)
    