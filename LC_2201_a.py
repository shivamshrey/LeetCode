# 2201. Count Artifacts That Can Be Extracted
# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(n)]
        count = 0
        
        for i, j in dig:
            grid[i][j] = 1  # mark as dug
                
        for r1, c1, r2, c2 in artifacts:
            excavatable = 1
            for i, j in itertools.product(range(r1, r2 + 1), range(c1, c2 + 1)):
                # even if one cell is not dug, the artifact can't be excavated
                if grid[i][j] == 0:
                    excavatable = 0
                    break
            count += excavatable
                        
        return count
    