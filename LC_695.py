# 695. Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        
        for u in range(m):
            for v in range(n):
                if grid[u][v] == 1:
                    count = max(self.dfs(grid, u, v), count)
        
        return count
    
    def dfs(self, grid, u, v):
        if u < 0 or u >= len(grid) or v < 0 or v >= len(grid[0]) or grid[u][v] != 1:
            return 0
        
        grid[u][v] = 0    # mark as visited
        
        return 1 + self.dfs(grid, u - 1, v) \
            + self.dfs(grid, u, v - 1) \
            + self.dfs(grid, u, v + 1) \
            + self.dfs(grid, u + 1, v)
    