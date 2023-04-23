# 1416. Restore The Array
# https://leetcode.com/problems/restore-the-array/description/

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        def dp(i):            
            if i == len(s): return 1
            if s[i] == '0': return 0
            if memo[i] != -1: return memo[i]
            result = 0
            for j in range(i, len(s)):
                if int(s[i:j + 1]) > k: break
                result += dp(j + 1)
            memo[i] = result % (10 ** 9 + 7)
            return memo[i]
        
        memo = [-1] * (len(s) + 1)
        return dp(0)
    