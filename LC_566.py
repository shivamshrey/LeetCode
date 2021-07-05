# 566. Reshape the Matrix

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        
        result = [[0 for j in range(c)] for i in range(r)]
        row, col = 0, 0
        for i in range(m):
            for j in range(n):
                result[row][col] = mat[i][j]
                col += 1
                if col == c:
                    row += 1
                    col = 0
        
        return result
        