# 1463. Cherry Pickup II
# https://leetcode.com/problems/cherry-pickup-ii/

# TC: O(N*M*M) * 9
# SC: O(N) + O(N*M*M)

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def helper(i, j1, j2):
            if j1 < 0 or j2 < 0 or j1 >= n or j2 >= n or i == m: return 0
            if dp[i][j1][j2] != -1: return dp[i][j1][j2]
            
            result = grid[i][j1]
            if j1 != j2: result += grid[i][j2]
            
            val = 0
            for d1 in (-1, 0, 1):
                for d2 in (-1, 0, 1):
                    val = max(val, helper(i + 1, j1 + d1, j2 + d2))
            
            dp[i][j1][j2] = result + val
            return dp[i][j1][j2]
        
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * n  for _ in range(n)] for _ in range(m)]
        return helper(0, 0, n - 1)
    