# 258. Add Digits
# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
        