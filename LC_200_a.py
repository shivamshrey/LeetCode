# 200. Number of Islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False for v in range(col)] for u in range(row)]
        
        count = 0
        for u in range(row):
            for v in range(col):
                if not visited[u][v] and grid[u][v] == '1':
                    self.numIslandsUtil(grid, u, v, visited)
                    count += 1
        
        return count
    
    def numIslandsUtil(self, grid: List[List[str]], u: int, v: int, visited: List[List[bool]]) -> None:
        visited[u][v] = True
        # row_num and col_num are used to get row and
        # column numbers of 8 neighbours of a given cell (u, v)
        row_num = [-1, 0, 0, 1]
        col_num = [0, -1, 1, 0]
        
        for k in range(4):
            if self.isSafe(grid, u + row_num[k], v + col_num[k], visited):
                self.numIslandsUtil(grid, u + row_num[k], v + col_num[k], visited)
        
        
    def isSafe(self, grid: List[List[str]], u: int, v: int, visited: List[List[bool]]) -> bool:
        return u >= 0 and u < len(grid) \
                and v >= 0 and v < len(grid[0]) \
                    and not visited[u][v] \
                        and grid[u][v] == '1'
    