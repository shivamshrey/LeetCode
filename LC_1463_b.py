# 1463. Cherry Pickup II
# https://leetcode.com/problems/cherry-pickup-ii/

# TC: O(N*M*M) * 9
# SC: O(N*M*M)

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:      
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * (n + 1)  for _ in range(n + 1)] for _ in range(m)]
        
        # Base case - Last/single row
        for j1 in range(n):
            for j2 in range(n):
                dp[m - 1][j1][j2] = grid[m - 1][j1]
                if j1 != j2: dp[m - 1][j1][j2] += grid[m - 1][j2]
        
        for i in range(m - 2, -1, -1):
            for j1 in range(n):
                for j2 in range(n):
                    dp[i][j1][j2] = grid[i][j1]
                    if j1 != j2: dp[i][j1][j2] += grid[i][j2]
                    val = 0
                    for d1 in (-1, 0, 1):
                        for d2 in (-1, 0, 1):
                            val = max(val, dp[i + 1][j1 + d1][j2 + d2])
                    dp[i][j1][j2] += val
                        
        return dp[0][0][n - 1]
    