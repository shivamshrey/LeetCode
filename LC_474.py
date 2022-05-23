# 474. Ones and Zeroes
# https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @functools.cache
        def dp(i, m, n):
            if i == len(strs):
                return 0
            
            counts = collections.Counter(strs[i])
            
            include = -1
            if m - counts["0"] >= 0 and n - counts["1"] >= 0:
                include = dp(i + 1, m - counts["0"], n - counts["1"]) + 1
            exclude = dp(i + 1, m, n)
            
            return max(include, exclude)
        
        return dp(0, m, n)