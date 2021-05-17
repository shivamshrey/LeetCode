# 994. Rotting Oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count_fresh = 0
        q = deque()
        
        # Enqueue rotten oranges, and count fresh ones
        for u in range(m):
            for v in range(n):
                if grid[u][v] == 2:
                    q.append((u, v))
                elif grid[u][v] == 1:
                    count_fresh += 1
        
        if count_fresh == 0:
            return 0
        
        # These 2 arrays are used to traverse
        # 4-directionally adjacent cells
        row_num = [-1, 0, 0, 1]
        col_num = [0, -1, 1, 0]
        count = 0
        while q:
            count += 1
            size = len(q)
            
            for i in range(size):
                u, v = q.popleft()
                # Check for all adjacent cells
                for j in range(4):
                    x = u + row_num[j]
                    y = v + col_num[j]
                    
                    if x < 0 or x >= m \
                        or y < 0 or y >= n \
                            or grid[x][y] == 2 \
                                or grid[x][y] == 0:
                        continue
                    
                    grid[x][y] = 2      # mark as rotten
                    count_fresh -= 1
                    if count_fresh == 0:
                        return count
                    q.append((x, y))    # enqueue newly rotten orange
        
        return -1
    