# 1143. Longest Common Subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # dp[i][j] = lcs(s1[0...i - 1], s2[0...j - 1])
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        # if m == 0
        for i in range(m + 1):
            dp[i][0] = 0

        # if n == 0
        for j in range(n + 1):
            dp[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i -1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
    