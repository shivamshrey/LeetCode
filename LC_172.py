# 172. Factorial Trailing Zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        i = 5
        while i <= n:
            result += n // i
            i *= 5
        
        return result
    