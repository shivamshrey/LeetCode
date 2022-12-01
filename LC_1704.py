# 1704. Determine if String Halves Are Alike
# https://leetcode.com/problems/determine-if-string-halves-are-alike/solution/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        for i in range(len(s) // 2):
            if s[i] in 'aeiouAEIOU': count += 1
            if s[len(s) - 1 - i] in 'aeiouAEIOU': count -= 1
        
        return count == 0
        