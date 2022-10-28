# 44. Wildcard Matching
# https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(p), len(s)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            dp[0][j] = False
        
        for i in range(1, m + 1):
            flag = True
            for ii in range(1, i + 1):
                if p[ii - 1] != '*':
                    flag = False
                    break
            dp[i][0] = flag
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False

        return dp[m][n]
    