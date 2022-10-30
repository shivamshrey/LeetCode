# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# TC: O(N * 4)
# SC: O(N * 5) + O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(i, transactions):
            if i == n or transactions == 0: return 0
            if dp[i][transactions] != -1: return dp[i][transactions]
            if transactions % 2 == 0:   # buy allowed
                dp[i][transactions] = max(-prices[i] + helper(i + 1, transactions - 1),
                                          helper(i + 1, transactions))
            else:                       # sell allowed
                dp[i][transactions] = max(prices[i] + helper(i + 1, transactions - 1),
                                          helper(i + 1, transactions))
            return dp[i][transactions]
        n = len(prices)
        dp = [[-1] * 5 for _ in range(n)]
        return helper(0, 4)
    