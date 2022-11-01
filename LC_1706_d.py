# 1706. Where Will the Ball Fall
# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = [0] * n
        
        for j in range(n):
            cur_col = j
            for i in range(m):
                next_col = cur_col + grid[i][cur_col]
                if (next_col < 0 or
                    next_col >= n or
                    grid[i][cur_col] != grid[i][next_col]):
                    result[j] = -1
                    break
                result[j] = next_col
                cur_col = next_col
        
        return result
    