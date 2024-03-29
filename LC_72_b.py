# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = [0] * (n + 1)
        cur = [0] * (n + 1)
        
        for j in range(n + 1):
            prev[j] = j
            
        for i in range(1, m + 1):
            cur[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])
            prev = cur[:]
        return prev[n]
    