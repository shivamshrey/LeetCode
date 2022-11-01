# 1706. Where Will the Ball Fall
# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        dp = [[-1] * n for _ in range(m + 1)]
        # Base case
        for j in range(n): dp[m][j] = j
        
        for i in range(m - 1, -1, -1):
            for j in range(n):
                next_col = j + grid[i][j]
                if (next_col < 0 or
                    next_col >= n or
                    grid[i][next_col] != grid[i][j]):
                    dp[i][j] = -1
                else:
                    dp[i][j] = dp[i + 1][next_col]
        
        return dp[0]
    