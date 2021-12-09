# 1314. Matrix Block Sum

# TC: O(m*n)
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # range_sum[i + 1][j + 1] corresponds to block sum till mat[i][j]
        range_sum = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                range_sum[i][j] = mat[i - 1][j - 1] + range_sum[i - 1][j] + range_sum[i][j - 1] - range_sum[i - 1][j - 1]
        
        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1, r2, c2 = max(0, i - k), max(0, j - k), min(m, i + k + 1), min(n, j + k + 1)
                answer[i][j] = range_sum[r2][c2] - range_sum[r1][c2] - range_sum[r2][c1] + range_sum[r1][c1]
        
        return answer               
        