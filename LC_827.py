# 827. Making A Large Island

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def neighbours(grid, i, j):
            for nrow, ncol in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                    yield nrow, ncol
                
        def dfs(grid, u, v, index):
            if (u < 0 or u >= len(grid) or 
                v < 0 or v >= len(grid[0]) or 
                grid[u][v] != 1):
                return 0
            
            # assign index (id) of current island
            grid[u][v] = index
            
            return 1 \
                + dfs(grid, u - 1, v, index) \
                + dfs(grid, u, v - 1, index) \
                + dfs(grid, u, v + 1, index) \
                + dfs(grid, u + 1, v, index)
        
        areas = dict()  # hashmap to store areas of all islands to avoid recalculation
        index = 2 # index starts from 2 as 0, 1 values are used for water & island
        for u in range(len(grid)):
            for v in range(len(grid[0])):
                if grid[u][v] == 1:
                    areas[index] = dfs(grid, u, v, index)
                    index += 1
        
        # [0] if all cells are 0 i.e. no islands present
        result = max(areas.values() or [0])
        
        for u in range(len(grid)):
            for v in range(len(grid[0])):
                if grid[u][v] == 0:
                    # set is required to avoid adding area of same island
                    # multiple times
                    possible = set(grid[nrow][ncol] for nrow, ncol in neighbours(grid, u, v)
                                   if grid[nrow][ncol] > 1)
                    # sum up the areas of all neighbours
                    # add 1 as we are changing current cell's 0 to 1
                    # find the maximum such area
                    result = max(result, sum(areas[index] for index in possible) + 1)
                    
        return result
        