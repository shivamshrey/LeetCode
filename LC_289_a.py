# 289. Game of Life

# TC: O(mn)
# SC: O(mn)

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def countLiveNeighbours(i, j):
            nonlocal m, n
            count = 0
            offsets = [
                (-1, -1), (-1, 0), (-1, 1), (0, -1), 
                (0, 1), (1, -1), (1, 0), (1, 1)
            ]
            
            for row_offset, column_offset in offsets:
                row = i + row_offset
                column = j + column_offset
                if row >= 0 and row < m and column >= 0 and column < n \
                        and board_copy[row][column] == 1:
                    count += 1
            
            return count
        
        m = len(board)
        n = len(board[0])
        board_copy = copy.deepcopy(board)
        
        for i in range(m):
            for j in range(n):
                count = countLiveNeighbours(i, j)
                
                if board_copy[i][j] == 0 and count == 3:
                    board[i][j] = 1
                elif board_copy[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = 0
        