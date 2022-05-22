# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.countPalindromes(s, i, i)
            result += self.countPalindromes(s, i, i + 1)
        return result
    
    def countPalindromes(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count