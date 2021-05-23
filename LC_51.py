# 51. N-Queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solution = []
        board = [['.' for j in range(n)] for i in range(n)]
        self.solveQueensUtil(n, 0, board, solution)
        return solution
        
    def solveQueensUtil(self, n, col, board, solution):
        if col == n:
            self.appendToSolution(board, solution)
            return True
        
        for row in range(n):
            if self.isSafe(row, col, board):
                board[row][col] = "Q"
                self.solveQueensUtil(n, col + 1, board, solution)
                board[row][col] = "."
            
        return False
    
    def isSafe(self, row, col, board):
        n = len(board)
        for j in range(col):
            if board[row][j] == "Q":
                return False
        
        i, j = row, col
        
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        
        i, j = row, col
        
        while i < n and j >= 0:
            if board[i][j] == "Q":
                return False
            i += 1
            j -= 1
                    
        return True
    
    def appendToSolution(self, board, solution):
        n = len(board)
        temp = []
        for i in range(n):
            temp.append("".join(board[i]))
        solution.append(temp)
        