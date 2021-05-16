# 200. Number of Islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        count = 0
        for u in range(row):
            for v in range(col):
                if grid[u][v] == '1':
                    self.numIslandsUtil(grid, u, v)
                    count += 1
        
        return count
    
    def numIslandsUtil(self, grid: List[List[str]], u: int, v: int) -> None:
        if u < 0 or u >= len(grid) or v < 0 or v >= len(grid[0]) or grid[u][v] != '1':
            return
        
        # mark it as visited
        grid[u][v] = '#'
        
        # Recur for all adjacent cells
        self.numIslandsUtil(grid, u - 1, v)     # up
        self.numIslandsUtil(grid, u + 1, v)     # down
        self.numIslandsUtil(grid, u, v - 1)     # left
        self.numIslandsUtil(grid, u, v + 1)     # right
    