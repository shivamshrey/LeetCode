# 2278. Percentage of Letter in String
# https://leetcode.com/problems/percentage-of-letter-in-string/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for char in s:
            if char == letter:
                count += 1
        return int((count / len(s)) * 100)