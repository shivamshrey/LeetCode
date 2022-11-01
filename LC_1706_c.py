# 1706. Where Will the Ball Fall
# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        nnext = [-1] * n
        cur = [-1] * n
        # Base case
        for j in range(n): nnext[j] = j
        
        for i in range(m - 1, -1, -1):
            for j in range(n):
                next_col = j + grid[i][j]
                if (next_col < 0 or
                    next_col >= n or
                    grid[i][next_col] != grid[i][j]):
                    cur[j] = -1
                else:
                    cur[j] = nnext[next_col]
            nnext = cur[:]
        return nnext
    