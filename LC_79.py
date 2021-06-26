# 79. Word Search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(word, c, i, j):
            nonlocal m, n
            if c == len(word):  # entire word is found
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == '#':
                return
            if board[i][j] != word[c]:
                return False
            
            char = board[i][j]
            board[i][j] = '#'   # mark as visited
            result = \
                backtrack(word, c + 1, i - 1, j) \
                or backtrack(word, c + 1, i, j - 1) \
                or backtrack(word, c + 1, i, j + 1) \
                or backtrack(word, c + 1, i + 1, j)
            
            board[i][j] = char  # restore original value
            return result
        
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if backtrack(word, 0, i, j):
                    return True
        
        return False
    