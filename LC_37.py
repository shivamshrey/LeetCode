# 37. Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.__solve_sudoku_util(board)
    
    def __solve_sudoku_util(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    for num in "123456789":
                        if self.__is_valid(board, i, j, num):
                            board[i][j] = str(num)
                            if self.__solve_sudoku_util(board): return True
                            board[i][j] = "."
                    return False
        return True
    
    def __is_valid(self, board, row, col, num):
        for i in range(9):
            if (board[i][col] == num or
                board[row][i] == num or
                board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num):
                return False
        return True
