# 73. Set Matrix Zeroes

# TC: O(mn)
# SC: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row = False   # marker for first row
        first_column = False    # marker for first column
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0: first_row = True
                    if j == 0: first_column = True
                    matrix[0][j] = 0    # mark in first row
                    matrix[i][0] = 0    # mark in first column
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_column:
            for i in range(m):
                matrix[i][0] = 0                    
        