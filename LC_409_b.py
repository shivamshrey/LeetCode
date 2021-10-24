# 409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum(count & 1 for count in collections.Counter(s).values())
        return len(s) - odds + bool(odds)
        