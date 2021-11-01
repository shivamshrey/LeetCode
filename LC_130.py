# 130. Surrounded Regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        def dfs(row, col):
            board[row][col] = 'Z'
            
            for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nrow, ncol = row + drow, col + dcol
                if nrow < 0 or nrow >= m or ncol < 0 or ncol >= n or board[nrow][ncol] != 'O':
                    continue
                dfs(nrow, ncol)
                
        def flip():
            for row in range(m):
                for col in range(n):
                    if board[row][col] == 'Z':
                        board[row][col] = 'O'
                    elif board[row][col] == 'O':
                        board[row][col] = 'X'
                        
        for row in (0, m - 1):
            for col in range(n):
                if board[row][col] == 'O':
                    dfs(row, col)
                    
        for row in range(m):
            for col in (0, n - 1):
                if board[row][col] == 'O':
                    dfs(row, col)
                    
        flip()
    