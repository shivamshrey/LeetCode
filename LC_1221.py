# 1221. Split a String in Balanced Strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        count = 0
        
        for ch in s:
            count += 1 if ch == 'L' else -1
            if count == 0:
                result += 1
        
        return result
    