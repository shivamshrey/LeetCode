# 576. Out of Boundary Paths

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(i, j, moves):
            if i < 0 or j < 0 or i == m or j == n:
                return 1
            if moves == 0:
                return 0
            
            result = \
                dfs(i - 1, j, moves - 1) + \
                dfs(i + 1, j, moves - 1) + \
                dfs(i, j - 1, moves - 1) + \
                dfs(i, j + 1, moves - 1)
            return result % 1_000_000_007
            
        return dfs(startRow, startColumn, maxMove)
    