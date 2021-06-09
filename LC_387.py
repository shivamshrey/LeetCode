# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        return -1
    