# 766. Toeplitz Matrix
# https://leetcode.com/problems/toeplitz-matrix/

# TC: O(M * N)
# SC: O(1)

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(matrix[i - 1][j - 1] == matrix[i][j]
                   for i in range(1, len(matrix))
                   for j in range(1, len(matrix[0])))
        