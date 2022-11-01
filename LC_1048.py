# 1048. Longest String Chain
# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def differs_by_one(s1, s2):
            if len(s1) - len(s2) != 1: return False
            i, j = 0, 0
            while i < len(s1):
                if j < len(s2) and s1[i] == s2[j]:
                    j += 1
                i += 1
            return True if j == len(s2) else False
        
        words.sort(key=len)
        n = len(words)
        dp = [1] * n
        result = 1
        for i in range(n):
            for j in range(i):
                if differs_by_one(words[i], words[j]) and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            result = max(result, dp[i])
        return result
    