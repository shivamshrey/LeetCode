# 115. Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def helper(i, j):
            if j < 0: return 1
            if i < 0: return 0
            if dp[i][j] != -1: return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = helper(i - 1, j - 1) + helper(i - 1, j)
            else:
                dp[i][j] = helper(i - 1, j)
            return dp[i][j]
        m, n = len(s), len(t)
        dp = [[-1] * n for _ in range(m)]
        return helper(m - 1, n - 1)
    