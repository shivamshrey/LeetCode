# 44. Wildcard Matching
# https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(i, j):
            if i < 0:
                return True if j < 0 else False
            if j < 0:
                for ii in range(i + 1):
                    if p[ii] != '*':
                        return False
                return True

            if dp[i][j] is not None: return dp[i][j]

            if p[i] == '?' or p[i] == s[j]:
                dp[i][j] = helper(i - 1, j - 1)
            elif p[i] == '*':
                dp[i][j] = helper(i - 1, j) or helper(i, j - 1)
            else:
                dp[i][j] = False
            return dp[i][j]

        m, n = len(p), len(s)
        dp = [[None] * n for _ in range(m)]
        return helper(m - 1, n - 1)
    