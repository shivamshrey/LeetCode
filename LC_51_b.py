# 51. N-Queens
# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(col=0):
            if col == n:
                result.append(append_solution(board))
                return
            
            for i in range(n):
                if (left_row[i] or 
                    lower_diagonal[i + col] or 
                    upper_diagonal[n - 1 + col - i]):
                    continue
                left_row[i] = lower_diagonal[i + col] = upper_diagonal[n - 1 + col - i] = True
                board[i][col] = 'Q'
                backtrack(col + 1)
                board[i][col] = '.'
                left_row[i] = lower_diagonal[i + col] = upper_diagonal[n - 1 + col - i] = False
        
        def append_solution(board):
            result = []        
            for row in board:
                result.append(''.join(row))
            return result
        
        board = [['.'] * n for _ in range(n)]
        left_row = [False] * n
        upper_diagonal = [False] * (2 * n - 1)
        lower_diagonal = [False] * (2 * n - 1)
        result = []
        backtrack()
        return result
