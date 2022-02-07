# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)
