# 36. Valid Sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if num + " found in row " + str(i) in seen \
                    or num + " found in column " + str(j) in seen \
                    or num + " found in block " + str(i // 3) + str(j // 3) in seen:
                        return False
                    seen.add(num + " found in row " + str(i))
                    seen.add(num + " found in column " + str(j))
                    seen.add(num + " found in block " + str(i // 3) + str(j // 3))
        
        return True
        