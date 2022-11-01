# 1706. Where Will the Ball Fall
# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def helper(i, j):
            if i == m: return j
            next_col = j + grid[i][j]
            if (next_col < 0 or
                next_col >= n or
                grid[i][next_col] != grid[i][j]):
                return -1
            return helper(i + 1, next_col)
            
        m, n = len(grid), len(grid[0])
        result = [-1] * n
        for j in range(n):
            result[j] = helper(0, j)
        return result        
    