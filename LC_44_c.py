# 44. Wildcard Matching
# https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(p), len(s)
        prev = [False] * (n + 1)
        cur = [False] * (n + 1)
        prev[0] = True
            
        for i in range(1, m + 1):
            cur[0] = self.__areAllStars(p, i)
            for j in range(1, n + 1):
                if p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                    cur[j] = prev[j - 1]
                elif p[i - 1] == '*':
                    cur[j] = prev[j] or cur[j - 1]
                else:
                    cur[j] = False
            prev = cur[:]

        return prev[n]
    
    def __areAllStars(self, p, i):
        for ii in range(1, i + 1):
            if p[ii - 1] != '*':
                return False
        return True
    