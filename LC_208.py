# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        self.isEnd = False
        self.children = dict()

    def insert(self, word: str) -> None:
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie()
            cur = cur.children[char]
        cur.isEnd = True              

    def search(self, word: str) -> bool:
        cur = self
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)