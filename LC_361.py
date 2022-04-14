# 361. Bomb Enemy
# https://leetcode.com/problems/bomb-enemy/

# TC: O(mn)
# SC: O(n)
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        col_kills = [0] * n
        result = 0
        
        for i in range(m):
            for j in range(n):
                # either first column or 'W' to the left of this cell
                # then recalculate row kills
                # from that cell onwards
                if j == 0 or grid[i][j - 1] == 'W':
                    row_kills = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        elif grid[i][k] == 'E':
                            row_kills += 1
                
                # either first row or 'W' above this cell
                # then recalculate column kills
                # from that cell onwards
                if i == 0 or grid[i - 1][j] == 'W':
                    col_kills[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        elif grid[k][j] == 'E':
                            col_kills[j] += 1
                
                if grid[i][j] == '0':
                    result = max(result, row_kills + col_kills[j])
        
        return result
    