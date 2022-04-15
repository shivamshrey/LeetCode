# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        root = self.buildTrie(words)    # add all words to trie
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, result)
        
        return result        
        
    def buildTrie(self, words):
        root = Trie()
        for word in words:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = Trie()
                cur = cur.children[char]
            cur.word = word
        return root
    
    def dfs(self, board, i, j, root, result):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '#':
            return
        
        char = board[i][j]  # back-up current cell letter
        
        if char not in root.children:
            return
        
        root = root.children[char]
        if root.word != '': # A word is found
            result.append(root.word)
            root.word = ''    # Remove word from trie after adding to result
        
        board[i][j] = '#'   # mark as visited
        
        self.dfs(board, i - 1, j, root, result)
        self.dfs(board, i + 1, j, root, result)
        self.dfs(board, i, j - 1, root, result)
        self.dfs(board, i, j + 1, root, result)
            
        board[i][j] = char  # unmark as visited
    
class Trie:

    def __init__(self):
        self.isEnd = False
        self.children = dict()
        self.word = ""