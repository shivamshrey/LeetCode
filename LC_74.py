# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        
        level = -1
        
        for i in range(m):
            if matrix[i][0] <= target:
                level += 1
            else:
                break
        
        if level == -1:
            return False
        
        return target in matrix[level]
