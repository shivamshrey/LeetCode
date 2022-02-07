# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        diff += ord(t[-1])
        return chr(diff)
    