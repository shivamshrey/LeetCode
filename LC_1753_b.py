# 1753. Maximum Score From Removing Stones

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        return min((a + b + c) // 2, (a + b + c) - max(a, b, c))
    